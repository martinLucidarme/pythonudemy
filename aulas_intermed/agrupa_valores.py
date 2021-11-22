'''
Groupby - agrupando valores
'''
from itertools import groupby, tee
alunos = [
    {'nome':'LUIZ', 'nota':'A'},
    {'nome':'LETICIA', 'nota':'B'},
    {'nome':'ROSE', 'nota':'C'},
    {'nome':'MARIE', 'nota':'B'},
    {'nome':'JOANA', 'nota':'B'},
    {'nome':'EDUARDO', 'nota':'A'},
    {'nome':'ANDRE', 'nota':'C'},
    {'nome':'ANDERSON', 'nota':'D'},
    {'nome':'LINA', 'nota':'A'},
    {'nome':'LUIZ', 'nota':'A'},
    {'nome':'LETICIA', 'nota':'B'},
    {'nome':'ROSE', 'nota':'C'},
    {'nome':'MARIE', 'nota':'B'},
    {'nome':'JOANA', 'nota':'B'},
    {'nome':'EDUARDO', 'nota':'A'},
    {'nome':'ANDRE', 'nota':'C'},
    {'nome':'ANDERSON', 'nota':'D'},
    {'nome':'LINA', 'nota':'A'},

]

ordena = lambda item : item['nota']  # função lambda: para função faceis f(x) = x : x *2 por exemplo
alunos.sort(key = ordena)
for aluno in alunos:
    print(aluno)

alunos_agrupados = groupby(alunos, ordena)
for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)  # tem que copiar a lista senão o list() vai esgotar o iterador antes do for
    print(f'\n Alunos com {agrupamento}')
    qtd = len(list(va1))  # esse list()
    print(f'\t {qtd} alunos tiraram a nota {agrupamento}')

    for aluno in va2:  # esse for
        print(aluno)