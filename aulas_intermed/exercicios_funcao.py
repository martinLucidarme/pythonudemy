"""
1 - Crie uma função saudação com paramêtro saudação e nome
"""

"""
2 - Crie uma função que recebe 3 num e soma entre eles
"""
"""
3 - crie uma função que recebe 2 num, um valor, um percentual
return o valor do primeiro + aumento percentual dele
"""
"""
4 - Fizz Buzz - Se o parametro da funcao for divisivel por 3
return fizz, se for por 5 return buzz, se for por 5 e 3 return FizzBuzz
contrario: return numero enviado
"""

# Ex 1:
def saudacao(saudaçao, nome):
    return f'{saudaçao}, {nome}'

print(saudacao('Ola', 'Martin'))

# Ex 2:
def soma3(n1,n2,n3):
    return n1+n2+n3

print(soma3(2,5,8))

# Ex 3:
def aumento(valor, percentual):
    return valor+percentual*valor/100

print(aumento(25,10))

# Ex 4:
def fizzbuzz(numero):
    b = False
    c = False
    msg = str(numero)
    if numero % 5 == 0:
        b = True
        msg = 'fizz'
    if numero % 3 == 0:
        c = True
        msg = 'buzz'
    if b and c:
        msg = 'FizzBuzz'
    return msg

print(fizzbuzz(10))
print(fizzbuzz(12))
print(fizzbuzz(15))
print(fizzbuzz(11))

# Ex 4 corrigido:

print('------ Corrigido -----')

def fizzbuzz2(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    if numero % 3 == 0:
        return 'fizz'
    if numero % 5 == 0:
        return 'buzz'
    return numero

from random import randint


print(fizzbuzz2(randint(0,100)))
print(fizzbuzz2(randint(0,100)))
print(fizzbuzz2(randint(0,100)))
print(fizzbuzz2(randint(0,100)))
print(fizzbuzz2(randint(0,100)))