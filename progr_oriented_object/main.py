from pessoa import Pessoa
#  p1 e p2 são as chamadas instâncias
p1 = Pessoa('Luiz', 29)  # método init para colocar as variáveis direto nos parametros de Pessoa()
p2 = Pessoa('Joana', 32)

p2.outro_metodo()  # metodo usa o self.nome do init
print()

p1.comer('maçã')
p1.comer('lamen')
p1.parar_comer()
p1.parar_comer()
p1.comer('feijao')
p1.falar('POO')
p1.parar_comer()
p1.falar('Brasil')
p1.parar_falar()
p1.falar('futebol')
p1.comer('miojo')

print()
print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)  # ano atual é da class entao não muda com a pessoa

p1.ano_de_nascimento()
p2.ano_de_nascimento()
