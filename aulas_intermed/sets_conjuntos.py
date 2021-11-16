# add, update,clear,discard
# union |
# intersection & (todos os elementos nos 2 sets)
# difference - (elementos so no set da esquerda)
# symmetric difference ^ (elementos nos dois sets mas nao em ambos)
# set: imutáveis, nao tem indice, sem elementos duplicados

s = {1, 2, 3, 4, 5}  # criar set com chaves, parece dict
no_empty_set = {}  # isso é um dicionario
s1 = set()
s1.add(1)
s1.add(2)
s1.update('a')  # adiciona elemento mo fim
s1.discard(1)  # tira elemento

print(s1)
for v in s1:  # pode iterar no set
    print(v)


s2 = set()
s2.update('Python')  # não respeita ordem
print(s2, 'update Python  - - - - - -')
s2.update([1,2,3,4],{1,2,3})
print(s2, 'S2 lista set - - - - - - -')

# set pode ser utilizado para eliminar duplicados da lista:
l1 = [1,2,1,1,2,2,3,3,6,6,5,4,4,8,8,5,5,9,9,8,4,1,1,2,3,'Luiz','Luiz','Luiz']
l1 = set(l1)
l1 = list(l1)

print(f'l1 é {l1}')  # cuidado q vai perder a ordem

# funções do set

s1 = {1,2,3,4,5,8}
s2 = {1,2,3,4,5,6,7}
s3 = s1 | s2
print(f's3 unido = {s3}')
s3 = s1 & s2
print(f's3 intersection = {s3}')
s3 = s1 - s2
print(f's3 diference = {s3}')  # elementos do set da esquerda q nao ta na direita
s3 = s1^s2
print(f's3 simmetric diff = {s3}')

l2 = ['Luiz', 'João', 'Maria','Luiz','Luiz','Luiz','Luiz']
l3 = ['Luiz', 'Maria','Maria','Maria','Maria','Maria','João']

l2 = set(l2)
l3 = set(l3)
if l2 == l3:  # retorna True pois tirou os duplos e a ordem
    print('L2 é igual a L3')
else:
    print('L2 é diferente L3')
print( list(l2), list(l3))
