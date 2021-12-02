'''
modulo com funções para:
- limpar o cnpj : só num
- fazer soma da contagem x cnpj
- gerar os digitos
- adiciona o digito no fim
- comparar os cnpj
- criar um cnpj aleatorio
- gerar um novo cnpj
'''

from random import randint


def remover_caracteres(cnpj):  # limpa o CNPJ para só numeros
    cnpj_limpo = ''
    nums = '0123456789'
    for i in cnpj:
        if i in nums:
            cnpj_limpo += i
    return cnpj_limpo


def soma_cnpj(cnpj_test, contagem_regressiva):  # faz a soma dos numeros e da contagem
    '''

    :param cnpj_test: cnpj limpo para testar
    :param contagem_regressiva: contagem regressiva com mesmo tamanho do cnpj
    :return: soma dos numeros do cnpj x contagem
    '''

    soma = 0
    tamanho = range(len(cnpj_test))
    for i in tamanho:
        multiplo = int(cnpj_test[i]) * int(contagem_regressiva[i])
        soma += multiplo
    return soma


def digitos(soma):  # gera o digito final

    formula = 11 - (soma % 11)

    if formula > 9:
        return '0'
    else:
        return str(formula)


def add_digit(cnpj_test, contagem_regressiva):  # adiciona o digito a cnpj a testar
    soma = soma_cnpj(cnpj_test, contagem_regressiva)
    digit = digitos(soma)
    cnpj_test += digit
    return cnpj_test


def compare_cnpj(cnpj_original):  # compara o cnpj enviado ao cnpj com digitos gerados pelo programa
    cnpj_original_limpo = remover_caracteres(cnpj_original)
    cnpj_test = cnpj_original_limpo[0:12]

    contagem1 = '543298765432'
    if not len(cnpj_test) == len(contagem1):
        return f'{cnpj_original} é um CNPJ inválido, o tamanho desse CNPJ está errado'
    cnpj1 = add_digit(cnpj_test, contagem1)

    contagem2 = '6543298765432'
    cnpj_final = add_digit(cnpj1, contagem2)

    if cnpj_final == cnpj_original_limpo:
        return f'\t{cnpj_original} é um CNPJ válido'
    else:
        return f'{cnpj_original} é um CNPJ inválido'


def cnpj_aleatorio():
    cnpj_aleat = ''
    cnpj_aleat += str(randint(0, 9)) + str(randint(0, 9)) + '.'
    cnpj_aleat += str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + '.'
    cnpj_aleat += str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + '/' + '0001' + '-'
    return cnpj_aleat


def generate_cnpj():  # Gera um cnpj valido
    cnpj_sem_digito = cnpj_aleatorio()
    cnpj_original_limpo = remover_caracteres(cnpj_sem_digito)
    cnpj_test = cnpj_original_limpo[0:12]

    contagem1 = '543298765432'
    if not len(cnpj_test) == len(contagem1):
        return f'{cnpj_sem_digito} é um CNPJ inválido, o tamanho desse CNPJ está errado'
    cnpj1 = add_digit(cnpj_test, contagem1)

    contagem2 = '6543298765432'
    cnpj_final = add_digit(cnpj1, contagem2)
    cnpj_final_bonito = cnpj_sem_digito + cnpj_final[-2] + cnpj_final[-1]
    return cnpj_final_bonito

