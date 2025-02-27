from abc import ABC, abstractmethod

class Personaje(ABC):
    @abstractmethod
    def __init__(self,nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.vida = 100
    @abstractmethod
    def atacar(self,objetivo):
        pass
    @abstractmethod
    def getestatus(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")

    def subirDeNivel(self):
        self.nivel+=1

    def verInventario(self):
        print(f"Inventario de {self.nombre}")
        for objeto in self.inventario:
            print(objeto)
class Mago(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.vida = 100
        self.inteligencia = 95
        self.inventario = ["grimorio","Pocion de mana"]

    def getestatus(self):
        print("Es de la clase Mago")
        super().getestatus()
    def atacar(self,objetivo):
        objetivo.vida -=self.inteligencia*0.6
        print(f"Vida actual del objetivo enemigo {objetivo.nombre} es {objetivo.vida}")
class Guerrero(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.inventario = ["Pocion de vida","escudo","espada"]
    def getestatus(self):
        print("Es la clase guerrero")
        super().getestatus()
    def atacar(self,objetivo):
        objetivo.vida -= self.fuerza * 0.8
        print(f"Vida actual del objetivo enemigo {objetivo.nombre} es {objetivo.vida}")

guerrero = Guerrero("Kaladin")
mago = Mago("Yuno")
print()
guerrero.getestatus()
mago.getestatus()
print()
guerrero.verInventario()
mago.verInventario()
print()
mago.atacar(guerrero)
guerrero.atacar(mago)