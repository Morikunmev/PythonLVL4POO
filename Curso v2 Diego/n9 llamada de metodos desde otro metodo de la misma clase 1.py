class Operaciones:
    def __init__(self):
        self.valor1 = int(input("valor 1: "))
        self.valor2 = int(input("valor 2: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.division()
    def sumar(self):
        suma = self.valor1 + self.valor2
        print("La suma es: ",suma)
    def restar(self):
        resta = self.valor1 - self.valor2
        print("la resta es: ",resta)
    def multiplicar(self):
        multi = self.valor1 * self.valor2
        print("la multiplicacion es: ",multi)
    def division(self):
        div = self.valor1 / self.valor2
        print("la division es: ",div)
operaciones1 = Operaciones()