# objetos mutaveis: listas e dict
# objetos imutaveis: tuplas, str, numeros, booleanos,

def lista_de_clientes(clientes_iteravel, lista=[]):
    # usando um arg mutavel lista = [], Python lê ele uma vez só e vai sempre adicionar tudo nesse
    # mesmo parametro, sempre vai adicionar neste 'lista'
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_de_clientes(['Joao', 'Maria', 'Lina'])
clientes2 = lista_de_clientes(['Rosa', 'Marcos', 'Ligia'])

print(clientes1)
print(clientes2)  # listas foram unidas: todos os nomes em todas as listas

# posso fazer assim: colocar uma lista minha invés do padrão
lista_sub = ['Martin']
clientes3 = lista_de_clientes(['A','B','C'], lista_sub)
print(clientes3)

# posso corrigir melhor assim:

def lista_de_corrigidos(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


corrig_clientes1 = lista_de_corrigidos(['Joao', 'Maria', 'Lina'])
corrig_clientes2 = lista_de_corrigidos(['Rosa', 'Marcos', 'Ligia'])

print(corrig_clientes1)
print(corrig_clientes2)