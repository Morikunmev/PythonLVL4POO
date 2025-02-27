from abc import ABC,abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.vida = 100
    @abstractmethod
    def atacar(self):
        pass
    def getinfo(self):
        print("nombre: ",self.nombre)
        print(f"edad: ",self.edad)
class Reptiliano(Persona):
    def __init__(self,nombre,edad, tipo_reptil,tamaño):
        super().__init__(nombre,edad)
        self.tipo_reptil = tipo_reptil
        self.tamaño = tamaño
        self.vida = 1000
        self.fuerza = 100
    def getinfo(self):
        print("FORMA HUMANA")
        super().getinfo()
        print("FORMA REPTILIANA")
        print("tipo reptil: ",self.tipo_reptil)
        print("Tamaño de reptil: ",self.tipo_reptil)

    def getvida(self):
        print(f"Puntos de vida: {self.vida}")
    def atacar(self,objetivo):
        objetivo.vida = objetivo.vida - self.fuerza * 0.4
        if objetivo.vida <=0:
            print(f"el {objetivo.nombre} ha muerto")
        else:
            print(f"el {objetivo.nombre} tiene {objetivo.vida} puntos de vida")
class ClasePura(Persona):
    def __init__(self,nombre,edad, tamaño):
        super().__init__(nombre,edad)
        self.tamaño = tamaño
        self.vida = 100
        self.fuerza = 12
    def getinfo(self):
        print("FORMA HUMANA")
        super().getinfo()
        print("FORMA PURA")
        print(f"tamaño: {self.tamaño}")
    def getvida(self):
        print(f"Puntos de vida: {self.vida}")
    def atacar(self,objetivo):
        objetivo.vida = objetivo.vida - self.fuerza * 0.1
        print(f"Vida actual del objetivo enemigo {objetivo.nombre} es {objetivo.vida}")
    def curarse(self):
        self.vida+=10*0.7
        print(f"{self.nombre} se ha curado 10 de vida, tiene en total {self.vida} de vida")

reptil = Reptiliano("Tovias",23,"rudo",100)
persona = ClasePura("richard",24,160)
reptil.atacar(persona)
reptil.atacar(persona)
persona.curarse()
persona.curarse()
persona.curarse()
reptil.atacar(persona)
