from classes1_asso import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Joazim')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
maquina.escrever()
print()
print('----- Associação de class: ------')
escritor.ferramenta = maquina  # associando a ferramenta ao escritor.
escritor.ferramenta.escrever()

del escritor
#print(escritor)  # escritor deixou de existir -> vai dar erro
print(caneta.marca)  # caneta (e maquina) ainda existe: associação 'fraca'
