""""
Combinations, Permutations and Products - itertools
Combi - Ordem nao importa
Permut - ordem importa
ambos nao repet valor unico
Produto - Ordem importa e repet valores unicos

"""
from itertools import combinations, permutations, product

pessoa = ['Luiz', 'André', 'Eduardo', 'Leticia', ' Fabricio', 'Rose']

for grupo in combinations(pessoa,3):  #  André Luiz e Luiz André são iguais, a ordem nao importa
    print(grupo)

for grupo in permutations(pessoa,2):  #  André Luiz e Luiz André são diferentes, ordem importa
    print(grupo)


for grupo in product(pessoa, repeat=2):  #  agora tem Luiz,Luiz, andré,andré... repete valores tb
    print(grupo)