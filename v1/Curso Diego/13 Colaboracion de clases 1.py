class Cliente:
    def __init__(self,nombre):
        self.nombre = nombre
        self.monto = 0
    def depositar(self,monto):
        self.monto = self.monto + monto
    def retornar(self):
        return self.monto
    def imprimir(self):
        print(self.nombre,"tiene depositado la suma de",self.monto)

class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Richard")
        self.cliente2 = Cliente("Skarlett")
        self.cliente3 = Cliente("Felipe")

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(200)
        self.cliente3.depositar(1000)
    def depositos_totales(self):
        total = self.cliente1.retornar() + self.cliente2.retornar() + self.cliente3.retornar()
        print("Total de dinero del banco: ",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
