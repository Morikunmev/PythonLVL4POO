class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def getinfo(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")