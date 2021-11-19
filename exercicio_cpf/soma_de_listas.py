'''
lista A e B duas listas de numeros
retorne lista dos valores somados

se lista maior que outra: retornar tamanho da menor
ex:
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

lista_soma = [2,4,6,8]
'''

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = [x+y for x, y in zip(lista_a,lista_b)]
print(lista_soma)
