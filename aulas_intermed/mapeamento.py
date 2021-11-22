'''

function map: recebe uma funcao de primeiro arg
'''

from dados import produtos, pessoas, lista

nova_lista = map(lambda x : x*2, lista)  # retorna um iterador
print(lista)
print(list(nova_lista),'\n')  # resultado bem parecido com um list comprehension

#  map() mais interessante para dict

##### Precos produtos ######

def aumenta_preco(p):
    p['preco'] = round(p['preco']*1.05, 2)
    return p

#precos = map(lambda p: p['preco'], produtos)  vai pegar o valor preco no dico produtos
precos_aumentados = map(aumenta_preco, produtos)  # lambda nao serve para funcao mais complexas

for produto in precos_aumentados:
    print(produto)

###### pessoas idades ######|

def aumenta_idade(p):
    p['nova_idade'] = p['idade'] * 1.20  # vai adicionar nova chave:valor no dict
    return p

nomes = map(aumenta_idade, pessoas)
for pessoa in nomes:
    print(pessoa)