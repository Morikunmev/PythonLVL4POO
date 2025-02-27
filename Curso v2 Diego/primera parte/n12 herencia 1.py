class Animal:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def alimentarse(self):
        print(self.nombre,"esta comiendo")
    def dormir(self):
        print(self.nombre,"esta durmiendo")

class Perro(Animal):
    def __init__(self,nombre,edad,raza):
        super().__init__(nombre,edad)
        self.raza = raza
    def ladrar(self):
        print(self.nombre,"esta ladrando")
class Gato(Animal):
    def __init__(self,nombre,edad,pelo):
        super().__init__(nombre,edad)
        self.pelo = pelo
    def maullar(self):
        print(self.nombre,"esta maullando")

perro1 = Perro("lucifer",2,"pitbull")
perro1.ladrar()

gato1 = Gato("Michi",2,"cafe")
gato1.maullar()























