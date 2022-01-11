"""
Java Script Object Notation - JSON
formato de troca de dados entre sistemas e programas
de forma muito leve e de fácil utilização
"""
from dados import *
import json

lista = [1, 2, 3, 4, 5, 6]
dados_json = json.dumps(lista)  # dumps converte para string
print(dados_json)  # dados_json é uma STR (py) array(JSON)

clientes_dados = json.dumps(clientes_dicionario, indent=4)  # formatação com identação padrão
print(clientes_dados)  # clientes_dados é um dict(Py) object(JSON)

dicionario = json.loads(clientes_json)  # converte a str JSON em dict Python
for chave, valor in dicionario.items():
    print(chave)
    print(valor)

print('====== colocar num arquivo json ======\n')

with open('clientes.json', 'w') as arquivo:  # criar o object no arquivo json com dict python
    json.dump(clientes_dicionario, arquivo, indent=4)  # agora é dump, não dumpS

with open('clientes.json', 'r') as file:  # colocar object json num dict py
    dados = json.load(file)  # agora é load, não loadS

for chave, valor in dados.items():
    print(chave, valor)
