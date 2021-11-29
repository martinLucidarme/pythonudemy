"""

formatação de preço

"""


def real(valor):
    return f'O preço é de R$ {valor:.2f}'.replace('.', ',')
