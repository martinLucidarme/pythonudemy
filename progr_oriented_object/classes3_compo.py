"""
relação mais fortes entre classes
uma class é dona de objeto da outra
class apagada = todos os objetos dela tb
"""

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))  # ISSO É A COMPOSICAO

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):  # serve para fazer algo qdo objeto é apagado
        print(f'{self.nome} foi apagado.')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}-{self.estado} foi apagado.')