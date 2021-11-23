
from ClassDog import Cachorro
from ClassBank import ContaBancaria

cachorro = Cachorro('rex', 10)

cachorro.sentar()
cachorro.rolar()

cachorro1 = Cachorro('leão', 5)

cachorro1.rolar()
cachorro1.sentar()

conta1 = ContaBancaria(1, 100)
print("Saldo da conta1:" + str(conta1.getSaldo()))

conta2 = ContaBancaria(2, 200)
print("Saldo da conta2:" + str(conta2.getSaldo()))

conta1.deposita(100)
print("Saldo da conta1:" + str(conta1.getSaldo()))

conta2.deposita(100)
print("Saldo da conta2:" + str(conta2.getSaldo()))

conta1.retira(50)
print("Saldo da conta1:" + str(conta1.getSaldo()))

conta2.retira(150)
print("Saldo da conta2:" + str(conta2.getSaldo()))
