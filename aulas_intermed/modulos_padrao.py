'''
Modulos padrão do python
arquivos.py para expandir as funcionalidades
https://docs.python.org/3/py-modindex.html
'''

import sys  # pode digitar 'from sys import ctrl+espaço para ver tudo
#  digitar 'sys.' pycharm vai mostrar tudo
print(sys.platform)
#  poderia ter feito 'from sys import platform'
# pode mudar nome tb
#  'from sys import platform as so'

from random import randint
print(randint(0, 10))  # nao precisa RANDOM.randint

def randint(*args):  #  se escrever func com msm nome: sobescreve
    return 'hahahaa'

for i in range(10):
        print(randint(0,10))
