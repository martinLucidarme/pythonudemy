'''
Comando no terminal para passar design.ui in python

pyuic5 design.ui -o design.py


'''

import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,  # onde vai abrir
            'Abrir Imagem',  # nome da janela
            r'C:\Users\Martin Lucidarme\Pictures',  # caminho inicial
            #  options= QFileDialog.DontUseNativeDialog
        )
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)  # nova imagem a partir da original,adapta a largura
        self.labelImg.setPixmap(self.nova_imagem)
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,  # onde vai abrir
            'Salvar Imagem',  # nome da janela
            r'C:\Users\Martin Lucidarme\Pictures\Saved Pictures',  # caminho inicial
            #  options= QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')  # Se nao passar por redimensionar nao vai ter nova imagem


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
