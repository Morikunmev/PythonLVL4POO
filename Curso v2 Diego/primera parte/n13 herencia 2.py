class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    def hablar(self):
        print(f"El animal que habla es {self.nombre}")
class Mamifero(Animal):
    def __init__(self,nombre,tipo_alim):
        super().__init__(nombre)
        self.tipo_alim = tipo_alim
    def comer(self):
        print(f"El animal come {self.tipo_alim}")
class Perro(Mamifero):
    def __init__(self,nombre,tipo_alim,raza):
        super().__init__(nombre,tipo_alim)
        self.raza = raza
    def imprimir(self):
        print("El perro",self.nombre,self.tipo_alim,self.raza)
    def comer(self):
        super().comer()
class Gato(Mamifero):
    def __init__(self,nombre,tipo_alim,tipo_pelo):
        super().__init__(nombre,tipo_alim)
        self.tipo_pelo = tipo_pelo
    def imprimir(self):
        print("El gato",self.nombre,self.tipo_alim,self.tipo_pelo)
    def comer(self):
        super().comer()
perro1 = Perro("Cachupin","Carnivoro","Chow-chow")
gato1 = Gato("Michi","Omnivoro","Angora")

perro1.imprimir()
gato1.imprimir()

perro1.comer()