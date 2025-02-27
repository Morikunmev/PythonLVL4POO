import math
class Circulo:
    def __init__(self):
        self.radio = int(input("ingrese el radio: "))
    def calculo_area(self):
        area = math.pi * self.radio ** 2
        area = round(area,2)
        print("El area es: ",area)
    def calculo_perimetro(self):
        perimetro= 2*math.pi*self.radio
        perimetro = round(perimetro,2)
        print("El perimetro es: ",perimetro)
circulo1 = Circulo()
circulo1.calculo_perimetro()
circulo1.calculo_area()