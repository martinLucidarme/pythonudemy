from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x>5, lista)
print(list(nova_lista))

nova_lista2 = filter(lambda p: p['preco'] > 50, produtos)  # filter: booleano, lista/dict

##### Produtos #####

for produto in nova_lista2:
    print(produto)

def filtra(produto):
    if produto['preco'] > 50:
        produto['é_caro'] = True
        return True

nova_lista3 = filter(filtra, produtos)

for produto in nova_lista3:
    print(produto)

##### Pessoas #####

def filtra_pessoa(pessoa):
    if pessoa['idade'] < 18:
        return True

lista_pessoa = filter(filtra_pessoa, pessoas)

for pessoa in lista_pessoa:
    print(pessoa)