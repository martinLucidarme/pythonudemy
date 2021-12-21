class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.poupanca = {}
        self.corrente = {}

    def cp_do_cliente(self, cp):
        self.poupanca = {'agencia': cp.agencia, 'conta': cp.conta, 'saldo': cp.saldo}

    def cc_do_cliente(self, cc):
        self.corrente = {'agencia': cc.agencia, 'conta': cc.conta, 'saldo': cc.saldo, 'limite': cc.limite}
