class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod  # definindo o metodo de class
    def por_ano_nascimento(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

#  metodo de class: usado para "melhorar uma class", por exemplo aqui, obter a idade só com o ano de nascimento


p1 = Pessoa('Luiz', 32)
p2 = Pessoa.por_ano_nascimento('Luizinho', 2001)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
p1.get_ano_nascimento()


