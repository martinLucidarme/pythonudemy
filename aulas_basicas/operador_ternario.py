"""
Operador ternário
"""

#  jeito complicado
logged_user = False
if logged_user:
    msg = 'Olá usuário. '
else:
    msg = 'Olá precisa logar.'

print(msg)

#  jeito operador ternario:

user_logged = True
msg2 = 'Usuario logado' if user_logged else 'Usuario precisa logar'
print(msg2)

# outro atalho

idade = input('Qual a sua idade')
if not idade.isnumeric():
    print('Você precisa digitar um número')
else:
    idade = int(idade)
    e_maior = (idade>=18)
    msg3 = 'Pode acessar' if e_maior else 'Não pode acessar'
    print(msg3)