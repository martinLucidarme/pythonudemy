"""
Split - dividir str em uma lista
Join - juntar uma lista numa str
Enumerate - associar elemento da lista com numero  # para objetos iteraveis, retorna tuplas

"""

# Split
string = "O Brasil é o país do futebol, o Brasil é penta, vai Brasil"
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor) # função count: conta qtas vezes o valor na lista

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

for valor in lista_2:
    print(valor.strip().capitalize()) # strip: tira espaço inicio e fim do str/ capitalize: primeira letra maiuscula


# Join

string2 = 'O Brasil é penta.'
listaa = string2.split(' ')
string3 = ','.join(listaa)  # junta elem da lista baseada no carater querido

print(string2)
print(listaa)
print(string3)

# Enumerate (cria um objeto enumerate: feito para ser iterado)
for indice, valor_real in enumerate(listaa):
    print(indice, valor_real) # valor real é a msm coisa q listaa[indice]

lista_de_lista =  [ [1,2],[3,4],[5,6]]
lista_simple = [2,4,6]
for i,v in lista_de_lista:
    print(i,v)
for a,b in enumerate(lista_simple): # Indice do enumerate comeca no 0
    print(a,b)

# Desempacotamento

lista = ['Luiz', 'João', 'Maria']
n1, n2, n3 = lista

print(n2)