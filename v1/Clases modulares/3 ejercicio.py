from Validacion import generaldef

class Cuadrado:
    def __init__(self):
        self.lado=generaldef.enterodef("Ingresa un lado: ")
    def imprimir(self):
        print("Lado ingresado: ",self.lado)
    def calculo(self):
        self.perimetro=self.lado*4
        self.area=self.lado*self.lado
        print(self.perimetro)
        print(self.area)
cuadrado1=Cuadrado()
cuadrado1.imprimir()
cuadrado1.calculo()
