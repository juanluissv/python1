class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # encapsulacion  __

        def depositar(self, monto):
            self.__saldo += monto
        
        def retirar(self, monto):
            if self.__saldo >= monto:
                self.__saldo -= monto
            else:
                print("Saldo insuficiente")
        
        def obtener_saldo(self):
            return self.__saldo