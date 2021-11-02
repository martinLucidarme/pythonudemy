'''
while boolean
    bloco filho
    condição de saida

'''

# usar continue para pular partes num while
# usar break para sair do while

# exemplo: pular 3 na contagem

x = 0
while x<10:
    if x == 3:  # selecione a condição a ignorar
        x = x + 1  # tem que colocar para evitar infinite loop
        continue  # volta no while sem executar nada
    if x == 8:
        break # sai do while quand x == 8
    print(x)
    x += 1 # no infinite loop

print('acabou')

# usar um else num while:
y = 0
while y < 10:
    print(y)
    y+=1
    if y == 8:
        break
else:  # do something when leaving the while
    print(y)

print(f'While breaked with y = {y}')