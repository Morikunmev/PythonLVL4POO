import math
class FigurasPlanas:
    def __init__(self):
        self.figuras = {}
        self.ejecucion()
    def mostrar_menu(self):
        print("1.cuadrado")
        print("2.rectangulo")
        print("3.triangulo")
        print("4.circulo")
        print("5.mostrar datos")
    def ejecucion(self):
        opcion = 0
        while opcion !=6:
            self.mostrar_menu()
            opcion = int(input("Eliga una opcion: "))
            if opcion == 1:
                self.calculo_cuadrado()
            elif opcion == 2:
                self.calculo_rectangulo()
            elif opcion == 3:
                self.calculo_triangulo()
            elif opcion == 4:
                self.calculo_circulo()
            elif opcion == 5:
                self.monstrar_figuras()
    def calculo_cuadrado(self):
        lado = int(input("Ingrese lado: "))
        area = lado**2
        perimetro = 4 + lado
        print(f"El area es: {area}")
        print(f"El perimetro es: {perimetro}")
        self.figuras["cuadrado"]=(("area = ",area),("perimetro = ",perimetro))
        print()
    def calculo_rectangulo(self):
        base = int(input("Ingrese base: "))
        altura = int(input("Ingrese altura: "))
        area = base * altura
        perimetro = 2*(altura + area)
        print(f"Area: {area}")
        print(f"Perimetro: {perimetro}")
        self.figuras["rectangulo"]=(("area = ",area),("perimetro = ",perimetro))
        print()
    def calculo_triangulo(self):
        base = int(input("Ingrese base: "))
        altura = int(input("Ingrese altura: "))
        area = (base * altura) / 2
        lado1 = int(input("Ingrese lado 1: "))
        lado2 = int(input("Ingrese lado 2: "))
        perimetro = base + lado1 + lado2
        print(f"El area es: {area}")
        print(f"El perimetro es: {perimetro}")
        self.figuras["triangulo"]= (("area = ",area),("perimetro = ",perimetro))
        print()
    def calculo_circulo(self):
        radio = int(input("Ingrese el radio: "))
        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio
        print(f"El area del circulo es: {area}")
        print(f"El perimetro es: {perimetro}")
        self.figuras["circulo"]=(("area = ",area),"perimetro = ",perimetro)
        print()
    def monstrar_figuras(self):
        for i in self.figuras:
            print(i,self.figuras[i])


figura1 = FigurasPlanas()