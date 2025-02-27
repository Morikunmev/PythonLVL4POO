class Usuario:
    def __init__(self,nombre = None, pertenencia= False):
        self.nombre = nombre
        self.pertenencia = pertenencia
        self.cantidad = 1 if self.pertenencia else 0
    def tomardef(self,tomar):
        self.cantidad +=tomar
    def cantidaddef(self):
        return self.cantidad
    def imprimir(self):
        print(self.nombre,"tiene en su posesion",self.cantidad,"Libros")

class Biblioteca:
    def __init__(self):
        self.usuario1 = Usuario("Richard",True)
        self.usuario2 = Usuario("Felipe")
    def operar(self):
        self.usuario1.tomardef(2)
    def imprimir(self):
        self.usuario1.imprimir()

dato1 = Biblioteca()
dato1.operar()
dato1.imprimir()