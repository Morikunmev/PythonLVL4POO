class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Ingrese un valor 1: "))
        self.valor2 = int(input("Ingrese un valor 2: "))
    def sumar(self):
        suma = self.valor1 + self.valor2
        print("la suma de los 2 valores es: ",suma)
    def restar(self):
        resta = self.valor1 - self.valor2
        print("la resta es: ",resta)
    def multiplicar(self):
        mult = self.valor1 * self.valor2
        print("la multiplicacion es: ",mult)
    def dividir(self):
        try:
            div = self.valor1 / self.valor2
            print("la division es: ",div)
        except ZeroDivisionError:
            print("No es posible dividir por 0")