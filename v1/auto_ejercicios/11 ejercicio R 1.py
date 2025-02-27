class Persona:
    def __init__(self,nombre,edad,altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        print("Se ha crado la persona")
    def imprimir(self):
        print("Sus datos son")
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad,"Años")
        print("Altura: ",self.altura,"metos")

registro = 0
persona1 = Persona("Richard",24,160)
persona1.imprimir()
