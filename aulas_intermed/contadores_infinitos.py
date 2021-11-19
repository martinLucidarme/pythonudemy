'''

count - Itertools
'''

from itertools import count

contador = count()  # isso é um iterador sem fim, cuidando quando loop

# para parar:
for valor in contador:
    print(valor)
    if valor >= 10:
        break

contador_parametrado = count(start=5, step=- 0.1 )  # é possível ter um step negativo
for valor in contador_parametrado:
    print(round(valor,2))  # redonda 2 numeros flutuantes
    if valor >= 10 or valor <= 0:
        break
