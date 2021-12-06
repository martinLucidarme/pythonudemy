from random import randint


class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

    @staticmethod
    def gera_id():  # nao recebe cls ou self
        rand = randint(10000, 99999)
        return rand

#  metodo estatico é uma funcao 'normal' mas dentro da class e q funciona com cls E self


p1 = Pessoa('Luiz', 32)
p2 = Pessoa.por_ano_nascimento('Luizinho', 2001)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
p1.get_ano_nascimento()

print(Pessoa.gera_id())
print(p1.gera_id())
