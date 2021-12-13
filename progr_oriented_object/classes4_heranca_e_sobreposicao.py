"""
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno:  # muito igual à um cliente
    def __init__(self, nome, idade):
        self.nome = nome  # estamos se repetindo: ruim (imagina se tiver Prof, docteur, parentes...)
        self.idade = idade
Tem que achar o que tem em comum entre Aluno e Clientes : são pessoas

"""
'''
Ai usa a herança: a classe filha (Cliente) ta herdando tudo da class mãe (Pessoa)
'''


class Pessoa:  # chamada superclass
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__  # para mostrar que a1 != c1

    def falar(self):
        print(f'{self.nomeclasse} Falando...')


class Cliente(Pessoa):  # Cliente vai ter todos os attrib de Pessoa (é uma subclass)

    def comprar(self):
        print(f'{self.nomeclasse} Comprando...')  # apenas do cliente

    def falar(self):
        print('é o falar da classe Cliente')


class ClienteVIP(Cliente):  # temos Pessoa>Cliente>ClienteVIP
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):  # eu posso sobreescrever: ISSO É A SOBREPOSICAO
        super().falar()  # falar() do Cliente
        # ele vai chamar o falar() da superclass no caso: Cliente, se nao tiver metodo falar(): vai pra Pessoa
        Pessoa.falar(self)  # chama o falar() da class Pessoa diretamente, NAO ESQUECA O SELF
        print(f'{self.nome} {self.sobrenome} ta falando')  # depois executa o resto


class Aluno(Pessoa):

    def estudar(self):
        print(f'{self.nomeclasse} Estudando...')  # apenas do aluno
