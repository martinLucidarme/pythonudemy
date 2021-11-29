
from vendas.formatacao import preco


def aumento(valor, porcentagem, formata=False):
    r = valor + (valor*porcentagem/100)
    if formata:
        return preco.real(r)
    else:
        return r


def reducao(valor, porcentagem, formata=False):
    r = valor - (valor*porcentagem/100)
    if formata:
        return preco.real(r)
    else:
        return r
