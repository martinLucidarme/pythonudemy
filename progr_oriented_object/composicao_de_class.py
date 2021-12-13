
from classes3_compo import Cliente  # classes compostas: nem preciso importar endereco

clientes1 = Cliente('Luiz', 32)
print(clientes1.nome)
clientes1.inserir_endereco('BH','MG')
clientes1.lista_endereco()
del clientes1  # vai remover o Cliente E SEUS OBJETOS (Endereco no caso)

print()

clientes2 = Cliente('Maria', 55)
print(clientes2.nome)
clientes2.inserir_endereco('Salvador', 'BA')
clientes2.inserir_endereco('Rio', 'RJ')
clientes2.lista_endereco()
print()

clientes3 = Cliente('João', 19)
print(clientes3.nome)
clientes3.inserir_endereco('Niteroy', 'RJ')
clientes3.lista_endereco()
print()
print('----- fim do codigo -----')  # depois: todos os clientes apagados = todos os objetos tb (compo)
