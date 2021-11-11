
nome = input('Qual seu nome ?')

# complicado

if nome:
    print(nome)
else:
    print('Você nao digitou nada =(')

# facil:

print(nome or 'Você nao digitou nada =(')

# o OR para na primeira expressão verdadeira

print(nome or None or False or 'Não escreveu' or 'não vou aparecer')

# com variáveis:
a = 0 # 0 é false
b = None # None é false
c = False
d = [] # lista vazia é false
e = {} # dict vazia é false
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g
print(variavel)

variavel2 = a or g or c or d or e or f or b #  ele checa NA ORDEM
print(variavel2)