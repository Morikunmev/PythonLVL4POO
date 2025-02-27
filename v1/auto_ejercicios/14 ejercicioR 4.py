from mod1 import operaciones
class Persona:
    contador_personas = 0
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        Persona.contador_personas+=1

    def imprimir(self):
        print("Datos")
        print("Nombre",self.nombre)
        print("Edad",self.edad)
    def __str__(self):
        if operaciones.mayordef(self.edad):
            return "Mayor de edad"
        else:
            return "Menor de edad"

persona1 = Persona("Richard",18)
persona1.imprimir()
print(persona1)

persona2 = Persona("Richard",17)
persona2.imprimir()
print(persona2)

print(f"Se han creado {Persona.contador_personas} personas")