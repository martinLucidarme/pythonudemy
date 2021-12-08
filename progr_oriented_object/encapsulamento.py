#  encapsulamento serve para esconder seu codigo para proteger ele
"""
Outros Codigos:
public ( metodos, attr acessados dentro e fora da class)
protected ( acessados apenas dentro da class ou das filhas dela)
private ( acessados apenas dentro da class)
"""
""""
No Python: usa se convenções
_  private - (weak)  (mais sutil, pode chamar mas nao vem sugerido no pycharm)
__ private - pode acessar com _NOMEDACLASSE__nomeatributo -
(strong) o programa vai proibir usar fora da classe: se usar ele vai criar outro com msm nome: confuso

no geral, nao acessar variaveis _ e __ fora da classe
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property  # posso usar Getter para acessar a lista de dados fora da classe sem mexer com o __dados
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otavio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.apaga_clientes(2)
bd.lista_clientes()
#  bd._dados = 'Uma outra coisa' quebraria a class: não funciona mais os metodo por isso dados ta protegido por _
print(bd.dados)  # com getter eu posso acessar a base de dados sem mexer na classe
# bd.dados = 'Outro valor'  # nao pode ser utilizado pq nao tem setter
