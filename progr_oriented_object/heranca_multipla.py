class A:
    def falar(self):
        print('falando que estou em A')


class B(A):
    def falar(self):
        print('falando que estou em B')


class C(A):
    def falar(self):
        print('falando que estou em C')


class D(B, C):
    """
    Ai tem herança múltipla: ela tem tudo de B e de C
    problema do diamante: 1 classe herda de 2 classes que tem o mesmo metodo
    No caso, Ele busca da esquerda para direita
    Se tiver metodo com mesmo nome em D, ele usa o de D
    posso inverter a ordem assim: class D(C, B)
    """


d = D()
d.falar()  # ele vai usar o falar de B()

