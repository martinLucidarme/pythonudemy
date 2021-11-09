#  Índices
#       0123456789........................33
frase = 'o rato roeu a roupa do rei de roma' # remember: string is not mutable
tamanho_frase = len(frase)
contador = 0
nova_string = ''
input_letra = input('Qual letra deseja colocar maiuscula ?')
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_letra:
        nova_string += input_letra.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)