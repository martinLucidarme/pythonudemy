
lista = [
    ('chave','valor'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
    ('chave4', 'valor4'),
]

# d1 = {x: y for x, y in lista} mesma coisa que :
d1 = dict(lista)
print(d1)

d2 = {x: y*2 for x, y in lista}
d3 = {x: y.upper() for x, y in lista}
print(d2)
print(d3)

d4 = {x for x in range(5)}  # também funciona com set
print(type(d4))

d5 = {f'chave{x}':x**2 for x in range(5)}
print(d5)
