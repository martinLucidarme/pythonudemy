"""

for in

tem: break (out of loop) e continue ( pull to next loop)
range(start = 0, stop, step = 1)
while: utilizado para coisas que você não sabe o fim
For: para coisas finitas

"""

texto = 'Python'
nova_string = ''

for n, letra in enumerate(texto):  # enumerate = (indice,valor)
    print(n, letra)

for n in range(20,9,-1): # o stop não é incluido !!
    print(n)

for letra in texto:
    if letra == 't':
        continue
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)