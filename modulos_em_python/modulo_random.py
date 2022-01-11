import random
import string

inteira = random.randint(10, 20)
inteiro = random.randrange(500, 900, step=10)  # inteiro aleatorio entre A e B com step
flutuante = random.uniform(10, 20)
flutuante2 = random.random()  # float entre 0 e 1

lista = ['Luiz', 'Otavio', 'Maria', 'Rose', 'Danilo', 'Jenny']
sorteio = random.choice(lista)  # seleciona um item da lista
sorteio2 = random.choices(lista, k=2)  # seleciona um fatiamento da lista com X items
sorteio3 = random.sample(lista, 2)  # seleciona um fatiamento da lista com X items DIFERENTES um do outro

random.shuffle(lista)  # embaralha a lista
print(lista)

# Exemplo: gerar senha aleatoria com modulo str

letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%¨&*()_-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))  # join junta os valores da lista numa str com separador: ""

print(senha)
