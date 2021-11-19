'''
Zip - Unindo iteraveis
Zip_longest - Itertools
'''


from itertools import zip_longest, count

indice = count()  # gerador infinito que conta: cuidado com zip longest
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)  # cria um gerador
cidades_estados2 = zip(estados, cidades, indice)  # pode zipar mais de 2
print(cidades_estados)
print(list(cidades_estados2))
print(dict(cidades_estados))
#print(next(cidades_estados))
#print(next(cidades_estados))

for valor in cidades_estados:
    print(valor)


indice = count()
cidad_estad = zip_longest(cidades, estados)
print(list(cidad_estad))  # print(list()) so para ver, geralmente usado para iterar sobre
cidad_estad = zip(
    indice,
    cidades,
    estados,
)

for indice, cidade, estado in cidad_estad:
    print(indice, cidade, estado)

