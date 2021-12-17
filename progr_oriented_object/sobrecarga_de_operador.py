"""
Comportamento de operador é definido por métodos especiais
pode ser alterado com classes do usuario
"""
'''
print(2+2)  # Python sabe que retorna 4
print('2'+'2')  # Python sabe que retorna '22'
'''


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

# Preciso da sobrecarga para ensinar ao Python o que eu quero dizer qdo usar operador entre 2 Retangulo

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"  # isso nao é sobrecarga de operador

    def __add__(self, other):  # metodo builtin do '+'
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):  # signo <
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):  # signo >
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(10, 20)  # Retangulo é um objeto meu, nao é um objeto builtin (int, str,...)
r2 = Retangulo(10, 20)
r3 = r1 + r2  # O Python sozinho nao vai saber o q fazer com isso sem o metodo builtin alterado (sobrecarregado)
print(r3)  # o __repr__ permite uma visualização melhor
print(r1 > r3)   # o simbolo > foi sobrecarregado para poder ser utilizado com minhas classes
print(r2 < r3)
print(r1 == r2)
print(r1 == r3)
