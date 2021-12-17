'''
exemplo
arquivo = open('abc.txt', 'w')
arquivo.write('Alguma coisa')
arquivo.close()  # muitas vezes: esquece de fechar => usa um context manager
'''

from contextlib import contextmanager

"""
método sem importar nada
class Arquivo:
    def __init__(self, arquivo, modo):
        print('INIT')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Entrou na classe')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Saiu da classe')
        self.arquivo.close()  # automatiza o fechamento


with  Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')

"""


# OUTRA MANEIRA

@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()  # automatiza o fechamento


with abrir('abc2.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
