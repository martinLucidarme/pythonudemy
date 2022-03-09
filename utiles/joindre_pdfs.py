
import PyPDF2
import os

caminho_dos_pdfs = r'C:\Users\Martin Lucidarme\Dropbox\MEF\Administratif\Notes de frais\fev 2022'
# unindo pdfs

novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_file = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_file, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(rf'{caminho_dos_pdfs}\note_de_frais_fev.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
