'''
programa q peça digitar um nome inteiro, se nao for inteiro, digit: nao é inteiro
'''

numint = input('Digite um inteiro')
if numint.isdigit():
    numint = int(numint)
    half = numint/2
    try: # técnica meio errada, melhor um if com modulo (par: num%2 == 0)
        half.isdigit()
        print(f'{numint} é um número par')
    except:
        print(f'{numint} é um número impar')
else:
    print('não é inteiro')

'''
Programa que pergunte hora e segundo hora responde a saudação apropriada
'''
hora = input('Digite a hora')
minutos = input('Digite os minutos')
hora_int = int(hora)
if hora_int >= 0 and hora_int < 12:
    print('Bom Dia !\nSão '+ hora +' horas e '+ minutos + ' minutos')
elif hora_int >= 12 and hora_int<17:
    print('Boa Tarde !\nSão ' + hora + ' horas e ' + minutos + ' minutos')
else:
    print('Boa Noite !\nSão ' + hora + ' horas e ' + minutos + ' minutos')

'''
Programa q peça nome do usuario, se for menor q 4 letras: print 'seu nome é curto", 
entre 5 e 6 letras - normal, 
maior que isso: muito grande
'''

nome = input('Digite seu nome')
tam = len(nome)
if tam <= 4:
    print(f'Seu nome é curto, {nome} !')
elif tam ==5 or tam ==6:
    print(f'Seu nome é médio, {nome}')
else:
    print(f'Que nome grande ! {nome}')