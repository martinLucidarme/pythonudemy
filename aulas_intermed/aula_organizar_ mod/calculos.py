import math

PI = math.pi

def dobra_lista(lista):
    return[x*2 for x in lista]
def multiplica(lista):
    r = 1
    for i in lista:
        r*= i
    return r


"""
print(dobra_lista(lista))
print(multiplica(lista))
print(PI)
pode comentar os prints para nao aparecer qdo importar o modulo
"""
# print(__name__)  # vai mostrar 'main' se eu executar aqui
                 # vai mostrar 'calculos' se for chamado por outro script

#  Geralmente se usa if main para fazer o print apenas no script de interesse

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
