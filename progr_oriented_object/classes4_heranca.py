"""
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno:  # muito igual à um cliente
    def __init__(self, nome, idade):
        self.nome = nome  # estamos se repetindo: ruim (imagina se tiver Prof, docteur, parentes...)
        self.idade = idade
Tem que achar o que tem em comum entre Aluno e Clientes : são pessoas

"""
'''
Ai usa a herança: a classe filha (Cliente) ta herdando tudo da class mãe (Pessoa)
'''


class Pessoa:  # chamada superclass
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__  # para mostrar que a1 != c1

    def falar(self):
        print(f'{self.nomeclasse} Falando...')


class Cliente(Pessoa):  # Cliente vai ter todos os attrib de Pessoa (é uma subclass)

    def comprar(self):
        print(f'{self.nomeclasse} Comprando...')  # apenas do cliente


class Aluno(Pessoa):

    def estudar(self):
        print(f'{self.nomeclasse} Estudando...')  # apenas do aluno

