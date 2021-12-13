from classes4_heranca_e_sobreposicao import *

"""
Associação : Usa - Agregação : Tem - Composição : É dono  - Hérança : É
"""

c1 = Cliente('Luiz', 32)
c1.falar()

a1 = Aluno('Ana', 21)  # Usando os atrib de Pessoa
a1.falar()  # o metodo funciona para tudo mundo que é Pessoa

#  porém a1.falar() ainda é diferente de c1.falar

p1 = Pessoa('João', 24)
p1.falar()  # único método quele herdou porque herança vem de cima pra baixo
