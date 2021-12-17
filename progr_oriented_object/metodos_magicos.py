"""
https://rszalski.github.io/magicmethods/
metodos magicos: começa e acaba com dunder: __metodo__
"""


class A:

    def __new__(cls, *args, **kwargs):  # esse metodo constroi a class
        print('Eu sou o new')
        return super().__new__(cls)  # so chama a class msm

    def __init__(self):  # metodo de instancia
        print('Eu sou o INIT')

    def __call__(self, *args, **kwargs):  # faz class se comportar como função
        print(args)
        print(kwargs)
        resultado = 1
        for i in args:
            resultado *= i
        return resultado

    def __setattr__(self, key, value):  # chamado cada vez q configura um atributo
        self.__dict__[key] = value  # grava o valor no dict da class
        print(key, value)
        if key == 'sobrenome':
            self.__dict__[key] = 'Nao pode fazer isso'


a = A()
a(1, 2, 3, 4, 5, nome='Luiz')  # nao possivel sem o call (nao ta no init)
variavel = a(1, 2, 3, 4, 5)  # nao defini uma func a ser usada assim: a.func()
print(variavel)

a.nome = 'Luiz Otavio'
print(a.nome)  # nao executa sem o __setattr__
a.sobrenome = 'Martin'
print(a.sobrenome)  # foi barrado no __setattr__
