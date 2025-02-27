from mod1 import operacionesv2
class Persona:
    Contador = 0
    ListaNombre = []
    ListaEdad = []
    def __init__(self,nombre =None,edad = None,altura = None,sueldo= None):
        self.nombre = nombre
        self.edad = operacionesv2.edad19(edad)
        self.altura = operacionesv2.altura19(altura)
        self.sueldo = operacionesv2.sueldo19(sueldo)
    def datos(self):
        operacionesv2.ejercicio19(self.nombre,self.edad,self.altura,self.sueldo)

    def agregaciones(self):
        Persona.Contador+=1
        Persona.ListaNombre.append(self.nombre)
        Persona.ListaEdad.append(self.edad)

class BaseDatos:
    def __str__(self):
        return f"{Persona.Contador} personas creadas"

persona1 = Persona("Richard",24,2.00,1.100)
persona1.datos()