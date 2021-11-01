''''
Formatando valores:

:s - strings
:d - Int
:f - float
:.(number)f - quantidade de casas decimais
:(CARACTER)(> ou < ou ^)(QUANTITY)(TYPE - s,d ou f)

> - esquerda
< - direita
^ - centro
'''
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao)) # deixar apenas 2 pontos flutuantes
print(f'{divisao:.2f}') # msma coisa

nome = 'Luiz Otávio'
print(f'{nome:s}')

num1=49.514
print(f'{num1:0>10}') #quero o num1 com 0 a ESQUERDA até preencher 10 casas

num2=1150
print(f'{num2:0<10}')