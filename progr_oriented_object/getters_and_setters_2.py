"""
Getter e setter são função
Setter = configurando um valor (=)
Getter = Obter um valor (.)
Getter apenas retorna o que foi configurado no Setter
pode ter apenas Getter
nao pode ter Setter sem Getter

Usado para editar classes
"""


class Pessoa:

    def __init__(self):
        self.atributo = 'inicial'

    @property  # nome vira um atributo, nao mais um método
    def nome(self):
        return self.atributo

    @nome.setter  # geralmente recebe um valor para configurar
    def nome(self, name):
        self.atributo = name


p1 = Pessoa()
p1.nome = 'Joao'
#  print(p1.nome()) nao funciona mais pq nome se comporta como attributo: nao callable
print(p1.atributo)
print(p1.nome)
