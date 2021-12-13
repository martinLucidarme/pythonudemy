class CarrinhoDeCompras:  # essa class precisa de produtos para existir
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:  # essa class pode existir sozinha
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
