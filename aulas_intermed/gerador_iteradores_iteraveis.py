'''
iteravel: lists, tuples, str -> sequences -> Iterável
'''
lista = [0,1,2,3,4,5]

'''
for v in lista:  # transforma a lista criando um iterador
    print(v)
'''

print(hasattr(lista,'__next__'))  # nao tem metodo

lista = iter(lista)  # a lista se tornou um iterador, agora tem metodo next
print(hasattr(lista,'__next__'))

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

import sys
import time

lista2 = list(range(10))  # tamanho da lista na memoria aumenta com tamanho pq armazena tds os valres ao msm tempo

'''
def gera(): # essa funcao ainda não é um gerador
    r  = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)  # espera 0.1 sec, simular opé pesada
    return r
'''
def gera():  # agora é um gerador
    for n in range(100):
        yield n
        #time.sleep(0.1)

g = gera()
print(g)  # agora é um gerador: retorna um valor de cada vez sem esperar o resto
for v in g:
    print(v)

print(hasattr(g,'__next__'))
print(hasattr(g,'__iter__'))

# exemplo
l1 = [x for x in range(1000)]  # com cochetes é lista ( ja salva todos os valores)
print(type(l1),sys.getsizeof(l1))
l2 = (x for x in range(1000))  # com parentese é gerador, tem q chamar o valor para ser salvo(for ou next)
print(type(l2), sys.getsizeof(l2))

# comportamento de iteradores e geradores:
# o gerador/iterador consome valor: uma vez utilizada no next() ou no for, nao pode mais chamar
# Exemplo:

nome = 'Zé_Ruella'
gerador = (letra for letra in nome)
print(next(gerador))
print(next(gerador))
print(next(gerador))
print('agora no for')
for letra in gerador: # letras RESTANTES no gerador/iterador
    print(letra)

print('outro for com gerador vazio')

for letra in gerador:
    print(letra)  # fosse iteraVEL, tinha printado de novo porque valores armazenados
