class CuentaBancaria:
    def __init__(self,saldo,cuenta):
        self.__saldo = saldo
        self.__cuenta = cuenta
    def getsaldo(self):
        return self.__saldo
    def getcuenta(self):
        return self.__cuenta
    def setsaldo(self,nuevo):
        if type(self.__saldo) == int or type(self.__saldo) == float:
            self.__saldo = nuevo
            print(f"El nuevo saldo es: {self.__saldo}")
    def setcuenta(self,nuevo):
        if type(self.__cuenta) == int:
            self.__cuenta = nuevo
            print(f"La nueva cuenta es: {self.__cuenta}")

class CuentaCorriente(CuentaBancaria):
    def __init__(self,saldo,cuenta,nombre):
        super().__init__(saldo,cuenta)
        self.__nombre = nombre
    def getnombre(self):
        return self.__nombre
c1 = CuentaCorriente(123123,12312321,"richard")
print(f"El saldo es {c1.getsaldo()}")
print(f"El nombre es {c1.getnombre()}")