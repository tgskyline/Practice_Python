class ContaBancaria():
    def __init__(self, codigo, saldo=0):
        self.codigo = codigo
        self.__saldo = saldo
    
    def deposita(self, quantia):
        self.__saldo += quantia
    
    def retira(self, quantia):
        if quantia < self.__saldo:
            self.__saldo -= quantia

    def getSaldo(self):
        return self.__saldo