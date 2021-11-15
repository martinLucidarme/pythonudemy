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
