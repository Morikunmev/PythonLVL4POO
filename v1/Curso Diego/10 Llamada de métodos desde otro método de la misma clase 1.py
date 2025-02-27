class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Ingrese primer valor: "))
        self.valor2 = int(input("Ingrese segundo valor: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.division()
    def sumar(self):
        suma = self.valor1 + self.valor2
        print("La suma es: ",suma)

    def restar(self):
        resta = self.valor1 - self.valor2
        print("La resta es: ",resta)
    def multiplicar(self):
        multiplicar = self.valor1 * self.valor2
        print("La multiplicacion es: ",multiplicar)
    def division(self):
        try:
            print("La division es: ", round(self.valor1 / self.valor2,2))
        except ZeroDivisionError:
            print("Error")

operacion1 = Operaciones()