"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from conta import ContaCorrente, ContaPoupanca
from clientes import Cliente
from banco import Banco

banco = Banco()
cli1 = Cliente('Martin', 26)
cli2 = Cliente('Maria', 28)
cli3 = Cliente('Lina', 46)
cli4 = Cliente('Lucas', 96)
cc1 = ContaCorrente(1254, 4456, 800)
cp1 = ContaPoupanca(1256, 1456, 540)
cc2 = ContaCorrente(1255, 4666, 8000)
cp2 = ContaPoupanca(1277, 1555, 5401)
cc3 = ContaCorrente(1288, 4444, 8020)
cp3 = ContaPoupanca(1299, 1333, 5440)
cc4 = ContaCorrente(1244, 4222, 8070)
cp4 = ContaPoupanca(1266, 1111, 54)

banco.add_info(cc1.conta, cc1.agencia, cli1)
banco.add_info(cc2.conta, cc2.agencia, cli2)
banco.add_info(cp3.conta, cp3.agencia, cli3)
banco.add_info(cp3.conta, cp3.agencia, cli3)

verif = banco.checagem(cc1.conta, cc1.agencia, cli1)
if verif:
    print('Você pode sacar')

