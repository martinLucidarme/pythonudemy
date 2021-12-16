from abc import ABC, abstractmethod


class A(ABC):  # Abstract Base Class
    @abstractmethod  # todas as classes que herdam de A vo ter que definir esse metodo
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando..B...')


a = B()
a.falar()
'''
a = A() # quando tem um abstract method na class , nao pode mais instanciar ela
b = B()  # nao poderia instanciar se nao tiver metodo falar em B
'''