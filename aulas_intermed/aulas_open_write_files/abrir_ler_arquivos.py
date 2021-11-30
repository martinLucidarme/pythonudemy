'''
https://www.docs.python.org/3/library/functions.html#open
'''

file = open('abc.txt', 'w+')

file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0,0)  # volta o 'cursor' no inicio do arquivo
print('Lendo linhas:')
print(file.read())  # sem o seek ele fica lendo o que tem depois do último write (lugar do 'cursor')
print('###########')

file.seek(0,0)
print(file.readline(), end='')  # lê uma linha e para o cursor ai
print(file.readline(), end='')  # end padrão: \n

file.close()
