class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - self.preco * (percentual / 100)

    # Getter  -  Getter e setters sao uma proteção sem precisar mexer no codigo da classe nem no main
    @property
    def preco(self):
        return self._preco  # coloca underline por convenção

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):  # testa se valor é uma str
            valor = float(valor.replace('R$', ''))  # tira as letras e transforma em float

        self._preco = valor

    # Outro exemplo
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title().replace('a', '@')


p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 'R$15')  # formato de preco não aceitado nesse codigo -> cria Getter/Setter
p2.desconto(10)
print(p2.nome, p2.preco)
