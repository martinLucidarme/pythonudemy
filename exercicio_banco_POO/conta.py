from abc import abstractmethod


class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor
        print(f'{valor} depositado, seu novo saldo é {self.saldo}')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        saldo_final = self.saldo - valor
        if saldo_final >= -self.limite:
            self.saldo = saldo_final
            return f'Seu saldo é agora de {self.saldo} (CC)'
        else:
            return f'Seu saldo de {self.saldo} é insuficiente para sacar {valor} com limite de {self.limite} (CC)'


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        saldo_final = self.saldo - valor
        if saldo_final > 0:
            self.saldo = saldo_final
            return f'Seu saldo é agora de {self.saldo} (CP)'
        else:
            return f'Seu saldo de {self.saldo} é insuficiente para sacar {valor} (CP)'
