class Triangulo:

    def inicializar(self):
        self.lado1 = int(input("Ingrese lado 1: "))
        self.lado2 = int(input("Ingrese lado 2: "))
        self.lado3 =int(input("Ingrese lado 3: "))
    def imprimir(self):
        print("lado 1: ",self.lado1)
        print("lado 2: ",self.lado2)
        print("lado 3: ",self.lado3)
    def lado_mayor(self):
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(self.lado1)
        elif self.lado2>self.lado1 and self.lado2>self.lado3:
            print(self.lado2)
        else:
            print(self.lado3)
    def equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")
triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.equilatero()

