class Banco:
    """
    Usa as classes clientes e banco
    """

    def __init__(self):
        self.agencias = []
        self.clientes = []
        self.contas = []

    def add_info(self, conta, agencia, cliente):
        if conta not in self.contas:
            self.contas.append(conta)
        else:
            print('conta ja cadastrada')
        if agencia not in self.agencias:
            self.agencias.append(agencia)
        else:
            print('agencia ja cadastrada')
        if cliente not in self.clientes:
            self.clientes.append(cliente)
        else:
            print('cliente ja cadastrado')

    def checagem(self, conta, agencia, cliente):

        if agencia not in self.agencias:
            print('Agencia nao cadastrada')
            return False
        if cliente not in self.clientes:
            print('Cliente nao cadastrado')
            return False
        if conta not in self.contas:
            print('conta nao cadastrada')
            return False
        else:
            print(f'tudo certo {cliente.nome}, bem vindo')
            return True
