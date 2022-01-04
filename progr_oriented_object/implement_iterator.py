"""
Como funciona a criação de lista

protocolo do iterator permite usar um for numa classe (nao so lista,etc..)
Impt: iter/next/setitem/getitem
"""


class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, val):
        self.__items.append(val)

    def __iter__(self):  # iter e next sao os 2 metodos no protocolo de definir iterator
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration  # necessario para parar a iteração qdo usar o for na classe

    def __getitem__(self, index):  # para poder usar anotação lista[x]
        return self.__items[index]

    def __setitem__(self, index, value):  # para poder setar o valor dum objeto no index
        if index >= len(self.__items):  # caso o index seja fora da lista(class) ja criada
            self.__items.append(value)
            return
        self.__items[index] = value

    def __delitem__(self, index):
        del self.__items[index]

    def __str__(self):  # permite exibir algo qdo printar a instancia lista
        return f'{self.__class__.__name__}({self.__items})'


if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('Martin')
    lista.add('Lina')

    print(lista)

    for valor in lista:  # possível esse for na INSTANCIA DA CLASS lista gracas ao protocolo iterator
        print(valor)

    print(lista[0])  # possivel gracas a __getitem__
    print(lista[1])
    lista[1] = 'Li'  # possivel gracas a __setitem__
    print(lista[1])
    lista[2] = 'Lin'
    lista[100] = 'Lind'
    lista[101] = 'MA'
    del lista[3]
    print(lista)
