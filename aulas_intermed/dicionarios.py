"""
Dicionarios em Python: {key : value}
Funcionamento bem similar as listas (indices...)
"""

d1 = {'chave1':'valor da chave'}  # isso é um dico
print(d1)

d1['nova chave'] = 'Valor da nova chave'  # pode adicionar valor/chave
print(d1)
d1['nova chave'] = 'Valor modificado'  # cada chave tem um só valor, valor pode ser modificado
print(d1)
print(d1['chave1'])  # pode usar indices

d2 = dict(chave1 = 'value of the key', chave2='value of other key')  #  outra maneira de criar dico
print(d2)
d2['nova chave'] = 'Valor da nova chave' # pode adicionar chave tb assim
print(d2)

# chave é algo imutável, geralmente str mas pode ser outro (até tupla)
d3 = { 'str': 'valor', 123: 'inteiro', (1, 2, 3): 'tupla'}
print( d3[(1,2,3)])

# print(d3['chave que nao existe']) = problema porque para o codigo
# resolve com if 'nao existe' in d1..., ai pode criar ela por exemplo
# tb pode usar d3.get('nomedachave') ai retorna um None, nao para o codigo

#  funções
d3.update({'nova chave':'novo valor' })  # mais facil com cochete
print(d3)
del d3['nova chave']
print(d3)
print(123 in d3)  # Booleans
print('inteiro' in d1.values())  # bool, busca uma valor
print(len(d3))
for k in d3:  # pode iterar no dicionario, no casos as chaves
    print(k)
for v in d3.values():  # no caso as valores
    print(v)
for i in d3.items():  # gera as tuplas
    print(i)
for a,b in d3.items():  # gera os valores separados
    print(a,b)
