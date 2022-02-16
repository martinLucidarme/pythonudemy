""""
Pilhas e filas
Pilha (stack) - LIFO - last in first out
    exemplo: pilha de livro adicionados um sobre o outro
Fila (queue) - FIFO - first in first out
    exemplo: fila do banco
filas podem ter efeitos colaterais em desempenho poraue a cada item alterado, todos
os índices serão modificados
"""
'''
JA VIMOS:

livros = list()
livros.append('Livro 1 ')
livros.append('Livro 2 ')
livros.append('Livro 3 ')
livros.append('Livro 4 ')
livros.append('Livro 5 ')
print(livros)
livro_removido = livros.pop()  # tira o livro emcima da pilha
print(livros, livro_removido)
# essa pilha é uma LIFO, ultimo que entra, primeiro sai
'''
# FIFO: cuidado que os indices mudam, quando a fila anda, cada posicao na fila muda
# usa se o modulo deque

from collections import deque  # modulo collections utilizado para trabalhar com gde qtd de dados
from time import sleep
fila = deque()  # crie uma lista FIFO
# exemplo com popleft
'''
fila.append('Joao')
fila.append('Joaozim')
fila.append('Joaozao')
fila.append('Joaozeiro')
fila.append('Joaozinho')

print(fila)

for nome in fila:  # comportamento igual lista
    print(nome)

tirado = fila.popleft()
print(fila, f' Saiu o {tirado}')
tirado = fila.popleft()
print(fila, f' Saiu o {tirado}')
tirado = fila.popleft()
print(fila, f' Saiu o {tirado}')
'''

fila2 = deque(maxlen=5)
fila2.extend([1,2,3,4])
fila2.append(5)
fila2.append(6)  # tira o um para colocar o 6: a fila anda.
fila2.insert(2,'Martin')  # insere o valor no indice 2
print(fila2)

'''
fila3 = deque(maxlen=10)
for i in range(1000):
    fila3.append(i)  # a fila vai andando
    sleep(0.5)
    print(fila3)
'''
# para ver todas as possibilidades: fila.'lista da possibilidades' (count, index, reverse...)
