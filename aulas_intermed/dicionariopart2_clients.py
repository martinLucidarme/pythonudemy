
clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otavio'
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira'
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Moreira'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')  # \t para identar

#  particularidade Python com dicionários
d1 = {1: 'a', 2: 'b', 3: 'c', 'lista': ['Luiz', 'Mariano']}
v = d1  # isso não cria um novo dicionario  (v==d1) is True

v[1] = 'Luiz'  # isso modifica d1 e v

print(d1)
print(v, '\n')
v = d1.copy()  # cria uma falsa copia
v[1] = 'nao é mais luiz'
v['lista'][0] = 'Modifica v e d1'
print(d1)  # v[1] foi modificado agora no v (str imutável),
print(v)  # a lista foi modif em v e d1: lista é mutável

import copy
print('-------- Deep Copy --------')
v = copy.deepcopy(d1)  # agora os dois são totalmente independentes
v[1] = 'nao é mais luiz'
v['lista'][0] = 'Modifica v apenas'
print(d1)  # v[1] foi modificado agora no v (str imutável),
print(v)  # a lista foi modif em v e d1: lista é mutável
