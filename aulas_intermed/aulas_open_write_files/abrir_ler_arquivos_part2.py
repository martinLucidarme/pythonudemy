'''
https://www.docs.python.org/3/library/functions.html#open
'''


import os
import json

"""
try:  # commum usar try para abrir arquivos, porém, nao muito Pythonico
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0,0)
    print(file.read())
finally:
    file.close()

"""

with open('abc2.txt', 'w+') as file:  # melhor maneira no Python
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0,0)
    print(file.read())

# outros modulos:
# open('file', 'a+') não apaga o arquivo: adiciona linhas

file2 = open('file2.txt','a+')
file2.write('outra linha sem apagar\n')
file2.write('outra linha sem apagar\n')
file2.close()

os.remove('file2.txt')  # pode deletar o arquivo

# open('file', 'r') so para ler o arquivo

# dict e json:

d1 = {
    'Pessoa 1': {
        'nome':'Luiz',
        'idade':25,
    },
    'Pessoa 2': {
        'nome':'Rose',
        'idade': 26,
    },
}

d1_json = json.dumps(d1, indent=True)  # passa o dico para json

with open('arquivo.json', 'w+') as djson:
    djson.write(d1_json)
    d2_json = json.loads(d1_json)

for k, v in d2_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1,v1)