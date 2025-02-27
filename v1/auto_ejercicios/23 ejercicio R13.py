from mod1 import valv2
class Alumno:
    def __init__(self,nombre = None, edad = None, sueldo = None):
        self.nombre = valv2.nombre23(nombre)
        self.edad = valv2.edad23(edad)
        self.sueldo = valv2.sueldo23(sueldo)
alumno1 = Alumno("","","r")
print(alumno1.nombre)
print(alumno1.sueldo)