"""
O modulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos como __init__(), __repr__(), __eq__()
em classes definidas pelo usuario
Dataclasses criam classes normais
doc: https://docs.python.org/pt-br/3/library/dataclasses.html
"""

from dataclasses import dataclass

'''
O dataclass vem assim: @dataclass(eq=True, repr=True, order=False, frozen=False, inti=True)
eq: pode usar = entre instancias
repr: formato bonito quando print(instancia)
order: habilita ou impede uso do sorted(), ou < e >
frozen: Torna a class imutável: impossível editar um valor
init: cria o metodo __init__
'''


@dataclass(repr=False)  # posso falar para ele tirar um metodo padrao
class Pessoa:  # isso é uma classe normal
    nome: str
    sobrenome: str

    @property  # posso colocar decorador
    def nome_completo(self):  # posso criar métodos
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Luiz', 'Otavio')
p2 = Pessoa('Luiz', 'Otavio')
print(p1 == p2)  # funciona pq método __eq__() ja vem escrito pela dataclass
print(p1)  # como eu tirei o repr da dataclass: vai aparecer com formatacao bruta
print(p1.nome_completo)
