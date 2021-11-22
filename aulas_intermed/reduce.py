from dados import produtos, pessoas, lista
from functools import reduce

'''
exemple
soma_lista = reduce(lambda ac,i:i+ac, lista,0)  # ACumulador, Item, 0= valor inicial
'''
soma_precos = reduce(lambda ac, p: p['preco']+ac, produtos,0)
print(soma_precos / len(produtos))

soma_idade = reduce(lambda ac, p: ac + p['idade'], pessoas,0)
print(soma_idade / len(pessoas))