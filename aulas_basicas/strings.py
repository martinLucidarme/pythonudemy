'''
nome = 'Martin'
idade = 25
peso = 80
altura = 1.76
imc = peso/altura**2

print(f'{nome} tem {idade} anos e um imc de {imc:.2f}')  # formatação float:2f para colocar apenas 2 num depois virgula
print('{} tem {} anos e um imc de {:.3f}'.format(nome,idade,imc))  # variaveis são utilizadas na ordem, pas fstring
print('{1} tem {2} anos e um imc de {0}'.format(nome,idade,imc))  # msm coisa mas segue ordem dada nas {}
print('{a} tem {b} anos e um imc de {c}'.format(a=nome,b=idade,c=imc))

'''
#Exercicio:
nome = 'Martin'
idade = 25
peso = 79.5
altura = 1.76
ano = 2021

imc = peso / altura**2
data= ano-idade
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kilos.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {data}')

#Índices e fatiamento
#Indices positivos de texto:  [012345678]
texto                     =   'Python s2'
#Indices negativos de texto: -[987654321]
# [ inicio : fim: pace ]
nova_string = texto[:6] #do 0 inicial até 6 nao incluido
print(nova_string)
print(texto[0::2])  # aqui o 2 é o pace
print(texto[:-1])  # útil para tirar ultimo carater
