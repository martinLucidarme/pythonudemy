import re #funções do professor


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


num1 = input('digite num')
num2 = input('digite outro num')

# 1 - funções Python
'''
# isnumeric isdigit isdecimal
# checagem numeros positivos inteiros
# print(num1.isnumeric())
# print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print (num2+num1)
else:
    print('Não pude converter os numeros para realizar a soma')
'''

# 2 - Funções do Professor
'''
if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)

    print (num2+num1)
else:
    print('erro do funções professor, use numeros')
'''

# Metodo try
try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1+num2)
except:
    print('Erro do try, use numeros')