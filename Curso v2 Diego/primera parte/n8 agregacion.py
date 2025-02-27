class Calculadora:
    numero = 0
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        Calculadora.numero = valor1
    def calculo_suma(self):
        return self.valor1 + Calculadora.numero + self.valor2
    def calculo_resta(self):
        return self.valor1 - Calculadora.numero - self.valor2
class Operacion:
    def __init__(self,nombre,valor):
        self.nombre = nombre
        self.valor = valor
    def retornar_valor(self):
        elige = int(input("Elige: "))
        if elige == 1:
            print(self.valor.calculo_suma())
        elif elige == 2:
            print(self.valor.calculo_resta())

calculadora1 = Calculadora(2,2)
operacion1 = Operacion("richard",calculadora1)
operacion1.retornar_valor()
