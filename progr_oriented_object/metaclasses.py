"""
tudo é objeto em Python, incluindo classes
metaclasses sao classes que criam classes
type é uma metaclasse
não é muito útil mas é bom conhecer
util para criar classes pra outras pessoas usar ou para design pattern
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):  # verifica se é método em B
                print(f'b_fala deve ser um método em {name}')

        return type.__new__(mcs, name, bases, namespace)  # cria a nova classe


class A(metaclass=Meta):  # class = molde, é um objeto tb
    attr = 'valor qlqr'

    def fala(self):
        self.b_fala()  # se nao tiver o b_fala na outra classe e chamar A, vai dar erro


class B(A):
    teste = 'Valor'
    pass

    def sei_la(self):
        pass

    def b_fala(self):
        print('Oi')


b = B()
