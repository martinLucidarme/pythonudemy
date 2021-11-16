"""
def
"""

def  funcao(msg='Olá', nome ='usuario'):
    nome = nome.replace('e','3') # procura o primeiro arg, troca por o segundo
    return msg, nome, 1, 2, 3, 4

variavel = funcao('ola', 'zezinho')
print(variavel)


def divisao(n1, n2):
    if n2 != 0:
        return n1/n2
    else: # vai retornar um tipo None se eu não colocar else
        return 'Não pode dividir por 0'

divide = divisao(8,2)
print(divide)
print(type(funcao()))
print(type(funcao))  # sem paranteses: a função não é executada

"""
Parte 3 - *args e **kwargs (conveções, poderia ser *ze, **ruela)
"""

# def func(a1, a2, a3, a4, a5, nome = None): arg sem padrão sempre antes dos arg com padrão
#     print(a1, a2, a3, a4, a5, nome)
#
# func(1,2,3,4,5, nome = 'Luiz')
#
def func(*args):
    print(args)  # args é uma tupla, não pode alterar itens dentro

    #args = list(args)  # transformo em lista para poder transformar
    #args[0] = 20
    #print(args)

lista = [1,2,3,4,5]
# n1, n2, *n = lista  # desempacota les 2 premiers, reempacota no n o resto
# print(n1,n2,n)
# print(*lista, sep = '-')  # pode escolher separador nos prints

func(lista)  # gera uma tupla com a lista em argumento 1
func(*lista) # desempacota diretamente a lista numa tupla
lista2= [48,49,50,51,52]
func(*lista, 10, 20, 30,40, *lista2)

# kwargs = key word arguments
def func2(*args, **kwargs):
    print(args)  # args é uma tupla, não pode alterar itens dentro
    print(kwargs)
    print(kwargs['sobrenome'])  # posso buscar um item pelo valor, da  erro senão tiver
    nome = kwargs.get('nome')  # melhor maneira de buscar pq nao da erro
    idade = kwargs.get('idade')
    if idade:
        print(idade)

func2(*lista, *lista2, nome='Luiz', sobrenome='Otavio', idade = '25' )
