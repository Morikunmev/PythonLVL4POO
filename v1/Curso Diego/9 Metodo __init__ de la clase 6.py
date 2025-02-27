class Operaciones:
    def __init__(self):
        self.valor1=int(input("Ingresa un valor: "))
        self.valor2=int(input("Ingresa otro valor: "))
    def calculo(self):
        print(f"La suma es: {self.valor1+self.valor2}")
        print(f"La resta es: {self.valor1-self.valor2}")
        print(f"La multiplicacion es: {self.valor1*self.valor2}")
        print(f"La division es: {self.valor1/self.valor2}")

operacion1 = Operaciones()
operacion1.calculo()
    
