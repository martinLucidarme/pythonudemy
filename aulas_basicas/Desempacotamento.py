""""
Desempacotar em Python
"""
'''
lista = ['Luiz','João','Maria']

n1, n2 = lista # erro ! too many values to unpack: 2 variav, 3 val na lista

print(n2)
'''

#  Resolvendo esse erro:

lista = ['Luiz','João','Maria',1,2,3,4,5,6,7,8,9,100]
n1, n2, n3, *_, ultimo = lista # pode usar qualquer *variavel mas convenção *_

print(n1, n2, ultimo)
print(n1, n2, _)