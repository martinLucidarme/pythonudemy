
from time import time
from time import sleep
"""
    ----   Bases sobre Funções   ----
def fala_oi():
    print('Falo Oi')


variavel = fala_oi
variavel()
print(type(variavel))


def master():
    def slave():  # posso criar uma função na função
        print('Ola')  #  print tb é uma funcao na funcao
    #slave()  # posso executar a função para ele aparecer qdo master for chamada
    return slave  # tambem posso retornar ela

variavel2 = master()
variavel2()
"""


def master(funcao):
    def slave(*args, **kwargs):  # tem q colocar a possibilidade de arg kwarg caso funcao decorada tenha args
        print('Agora estou decorada')
        funcao(*args, **kwargs)
    return slave


def fala_oi():
    print('Oi')


fala_oi = master(fala_oi)  # fala_oi é uma funcao decorada com a funcao master
fala_oi()  # se comentar linha de cima: nao ta mais deocrada

""" 

inves de colocar  a linha fala_oi = master(fala_oi) posso colocar
@master
em cima da funcao para decorar automaticamente:

"""

@master
def fala_oi2():
    print('mais um Oi')

@master
def outra_funcao(msg):
    print(msg)

fala_oi2()
outra_funcao('Ola eu sou Martin')  # tem q colocar parametro na slave() para nao dar pb


def velocidade(funcao):  # outro exemplo
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\n A função {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(5):
        print(i, end='')
        sleep(1)

demora()