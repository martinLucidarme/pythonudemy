from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))  # atributo de class
    # def falar(self):  # isso é um metodo
    #    print('Pessoa está falando')

    def __init__(self, nome, idade, comendo=False, falando=False):
        #  método init permite colocar as variáveis direto nos parametros de Pessoa()
        self.nome = nome  # essas variaveis sao atributos de instancia
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def outro_metodo(self):
        print(self.nome)  # os self do init sao definidos para todos os outros metodos

    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        self.comendo = True
        print(f'{self.nome} está comendo {alimento}')

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        self.falando = False
        print(f'{self.nome} parou de falar')

    def ano_de_nascimento(self):
        ano_nasc = int(self.ano_atual) - int(self.idade)
        print(f'{self.nome} nasceu em {ano_nasc}')
