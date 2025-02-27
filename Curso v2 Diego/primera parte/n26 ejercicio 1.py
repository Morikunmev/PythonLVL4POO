class Reptil:
    def __init__(self,nombre,patas,tamaño):
        self.nombre = nombre
        self.patas = patas
        self.tamaño = tamaño
    def imprimir(self):
        print(f"Nombre de la forma reptiliana: {self.nombre}")
        print(f"Numero de patas: {self.patas}")
        print(f"Tamaño: {self.tamaño}")
class Perro:
    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.raza = raza
    def getreptil(self,nombre,patas,tamaño):
        self.reptil = Reptil(nombre,patas,tamaño)
    def imprimir(self):
        print(f"nombre del perro: {self.nombre}")
        print(f"Raza del perro: {self.raza}")
    def imprimir2(self):
        self.imprimir()
        self.reptil.imprimir()



perro1 = Perro("richard","canino")
perro1.getreptil("reptiliano",4,150)
perro1.imprimir2()