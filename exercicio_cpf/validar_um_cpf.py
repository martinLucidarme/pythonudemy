""""
CPF = 168.995.350-09

1*10 = 10           # 1 * 11 = 11
6* 9 = 54           # 6 * 10 = 60
8 * 8 = 64          # 8 * 9 = 72
9 * 7 = 63          # 9 * 8 = 72
9 * 6 = 54          # 9 * 7 = 63
5 * 5 = 25          # 5 * 6 = 30
3 * 4 = 12          # 3 * 5 = 15
5 * 3 = 15          # 5 * 4 = 20
0 * 2 = 0           # 0 * 3 = 0
                    # 0 * 2 = 0

        297         #          343
11 - (297%11) = 11  # 11 - (343%11) = 9
11>9 = 0            #
Digito 1 = 0        # Digito 2 = 9

"""

# minha solução
cpf = input('Digite numeros do seu cpf sem pontos nem traço')
novo_cpf = cpf[:-2]
soma = 0

for i, numero in enumerate(novo_cpf):
    calc = int(numero) * (len(novo_cpf)-i+1)
    soma += calc
    mod = 11 - (soma % 11)
if mod > 9:
    novo_cpf += '0'
else:
    novo_cpf += str(mod)

soma1 = 0
cpf_transit = novo_cpf
for i, numero in enumerate(cpf_transit):
    calc1 = int(numero) * (len(cpf_transit)-i+1)
    soma1 += calc1
    mod1 = 11 - (soma1 % 11)
if mod1 > 9:
    cpf_transit += '0'
else:
    cpf_transit += str(mod1)

'''
print(soma)
print(mod)
print(novo_cpf)
print(soma1)
print(mod1)
print(cpf_transit)
'''
if cpf_transit == cpf:
    print('É nois cachorro')
else:
    print('cpf incorreto')