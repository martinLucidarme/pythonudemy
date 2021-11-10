"""
usar o for else: quase inútil
"""

# Caso complicado :

variavel = ['Luiz otávio','Toãozinho', 'Maria']
comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'): #  tira a diferença minus/maiusculo
        comeca_com_j = True

if comeca_com_j == True:
    print('Existe um nome que começa com J')
else:
    print('Não existe uma palavra q começa com J')

# Simplificação

variavel = ['Luiz otávio','AJoãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra q começa com J')