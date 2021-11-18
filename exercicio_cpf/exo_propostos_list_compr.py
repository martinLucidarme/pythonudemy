""""
separar todos os grupos de 0 a 9 para ficar assim

lista = ['0123456789','0123456789','0123456789','0123456789'...]
e depois
retorno = '0123456789.0123456789.0123456789...'
"""

string1 = '0123456789012345678901234567890123456789'
n = 10
lista = [string1[i: i+n] for i in range(0,len(string1),n)]
print(lista)
retorno = '.'.join(lista)
print(retorno)