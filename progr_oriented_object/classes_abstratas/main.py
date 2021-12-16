from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente

cp = ContaPoupanca(1125, 2658, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print('\n----- conta corrente -----\n')

cc = ContaCorrente(2582, 4564, 0, 500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
