# import vendas.calcula_preco  // nao facil de ler depois (vou ter q usar vendas.xxx)
#  from vendas import calcula_preco  // ainda não esta perfeito (vou ter q usar calcula_preco.xxx)
from vendas.calcula_preco import aumento, reducao
from vendas.formatacao import preco

preco1 = 49.90
preco_com_aumento = aumento(preco1, 15, formata=True)
print(preco_com_aumento)
preco_com_reducao = reducao(preco1, 15, formata=True)
print(preco_com_reducao)

print(preco.real(40))

