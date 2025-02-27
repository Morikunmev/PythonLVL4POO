def forma1():
    class Cuadrado:
        def __init__(self, lado):
            self.lado=lado
        def imprimir(self):
            print(self.lado)
        def calculo(self):
            self.perimetro=self.lado *4
            self.area=self.lado * self.lado
            print("Perimetro del cuadrado:",self.perimetro)
            print("Area del cuadrado:",self.area)

    cuadrado1 = Cuadrado(2)
    cuadrado1.imprimir()
    cuadrado1.calculo()


def forma2():
    def enterodef():
        while True:
            try:
                numero = int(input("Ingrese un lado: "))
                if numero==0:
                    continue
                return numero
            except ValueError:
                continue
    class Cuadrado:
        def __init__(self):
            self.lado=enterodef()
            
        def perimetrodef(self):
            return self.lado*4
        
        def areadef(self):
            return self.lado*self.lado
        
        def calculo(self):
            perimetro=self.perimetrodef()
            area=self.areadef()
            print("El perimetro del cuadrado es: ",perimetro)
            print("El area del cuadrado es: ",area)

    cuadrado1 = Cuadrado()
    cuadrado1.calculo()
forma2()

def forma3():
    class Cuadrado:
        def __init__(self,valor):
            self.valor=valor
        def calculo(self):
            perimetro=self.valor*4
            area=self.valor*self.valor
            print(f"El perimetro es: {perimetro}"),print(f"El area es: {area}")
    cuadrado1 = Cuadrado(2)
    cuadrado1.calculo()

