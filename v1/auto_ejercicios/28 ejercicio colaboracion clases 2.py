class Auto:
    def __init__(self,marca = None,color = None,ruedas = None):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas
    def imprimir(self):
        print("Marca: ",self.marca)
        print("Color: ",self.color)
        print("Ruedas: ",self.ruedas)
class Caracteristicas:
    def __init__(self):
        self.auto1 = Auto("Toyora","Azul")
        print("Marca: ",self.auto1.marca)
        print("Color: ",self.auto1.color)
        print("Ruedas: ",self.auto1.ruedas)

caracteristicas1 = Caracteristicas()

