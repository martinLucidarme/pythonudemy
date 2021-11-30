'''
https://www.docs.python.org/3/library/functions.html#open
'''

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
# open('file', 'r') so para ler o arquivo
