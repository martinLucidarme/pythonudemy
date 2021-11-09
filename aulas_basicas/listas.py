"""
Listas em Python
todos tipos de valor
lista = [1,2,3,4, 'Luiz Otávio', True, class]
fatiamento
append,insert,pop,del,clear,extend. +
min, max
range
"""

'''
Diferença lista / str e índices de lista
#         0    1    2    3    4
lista = ['A', 'Bacana', 'C', 'D', 'E']
#   -     5    4    3    2    1

string = 'ABacanaCDE'
print(string[1]) #  na string c consegue apenas acessar um solo valor q é str
print(lista[1]) #  A lista permite pegar vários valores de tipos diferentes
'''


lista = ['A', 'B', 'C', 'D', 'E', 10.5]
l1 = [1,2,3]
l2 = [4,5,6,7,8,9]

print(lista[5])
lista[5] = 'qlqr outra coisa'
print(lista[5]) # é possível modificar a propria lista, diferente de string
print(lista[0:3]) # o stop é excluido !!
print(lista[::-1]) # inverter a lista

lista_concat = lista + l2 # é possível adicionar listas
print(lista_concat)
#Extend adicionar vários elementos na propria lista:
l1.extend(l2) # adiciona OS valorES da lista
print(l1)

#Append insere UM SÓ novo valor NO FINAL
l2.append(l1) # adiciona UM valor 'lista'
print(l2)

# Insert insere UM elemento no índice desejado, tipo append

l2.insert(0,['manga','banana']) # insert ( indice, valor)
print(l2)

# Pop tira o ultimo item da lista:
l2.pop()
print(l2)

# Del tira uma fatia (ou um valor) nos indices desejados
del(l2[3:5])
print(l2)

'''
Aparte
 criar uma lista facilmente:
 list_1_to_9 = list(range(1,10, step = 1))
 pode iterar em listas:

l4 = [1,2,3,4,5,6,7,8,9]
for valor in l4:
    print(valor)
'''

# Exemplo do jogo adivinha palavra

secreto = 'perfume'
digitadas = [] # lista vazia
chances = 3
while True:

    if chances < 0 :   # condição de derrota
        print('Perdeu vacilão')
        break

    letra = input('Digite ume letra: ')
    if len(letra)> 1:
        print(' Tem que ser só uma letra rapai ')
        continue
    digitadas.append(letra) # armazena as letras digitadas enquanto o jogo dura

    if letra in secreto:
        print(f'Eba, {letra} existe na plavra secreta')
    else:
        digitadas.pop()
        print(f'Vacilou, {letra} não existe na palavra secreta \n sobra {chances} chances')
        chances -= 1

    secreto_temporario = ''  # esvazia a lista do print a cada laço
    for letra_secreta in secreto:  # checagem das letras da palavra uma por uma na ordem
        if letra_secreta in digitadas:  # a letra foi digitada pelo usuario
            secreto_temporario += letra_secreta # adiciona na lista do PRINT
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:  # condição de vitoria
        print(f'Parabéns, você ganhou um {secreto}, pois a palavra era {secreto}')
        break

    print(secreto_temporario)  # lista de ajuda do print, não de armazenamento (digitadas)
