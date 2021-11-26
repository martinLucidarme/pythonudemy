'''
import calculos  # tudo dentro do cálculo vai ser executado

print(calculos.PI)  # print esse e todos dentro de 'calculos'

'''

import calculos
print(calculos.PI)
lista = [2, 4]
print(calculos.multiplica(lista))

# posso tb fazer 'from modulo import algo'
# ai posso fazer algo(x) sem ter q fazer modulo.algo(x)
from outro import fala_oi

fala_oi()
