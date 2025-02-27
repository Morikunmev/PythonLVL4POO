from mod1 import operacionesv2

class Alumno:
    ListaNombre = []
    ListaEdad = []
    def __init__(self, nombre = None, edad = None):
        self.nombre = nombre
        self.edad = edad

        Alumno.ListaNombre.append(self.nombre)
        Alumno.ListaEdad.append(self.edad)

    def datos(self):
        operacionesv2.datosdef(self.nombre,self.edad)
    def mayoredad(self):
        operacionesv2.mayoredaddef(self.edad)

alumno1 = Alumno()
alumno1.mayoredad()