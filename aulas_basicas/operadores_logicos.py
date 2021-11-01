'''

operadores logicos: and,or, not
in,not in
'''
a=2
b=3
#  and : as duas precisam ser true para ter true
a and b

#  or : uma precisa ser true para ter true
a or b

# not : inversor, ele invert o valor
if b>a:
    print ('b é maior do que a')
else:
    print('a é maior que b')

if not b>a: #not transforma > em <
    print ('b é maior do que a')
else:
    print('a é maior que b')

# not usado tb para variavel vazia
v='' #funciona tb com v=0
w=4
if not v:
    v=input('please fill v \n')
if not v:
    v = input('please fill v')

#in e not in
nome = 'martin'
if 'a' in nome:
    print('tem a')
else:
    print ('não tem u')

if 'u' not in nome:  # not in = inversor tb
    print('nao tem u')
else:
    print ('tem u')