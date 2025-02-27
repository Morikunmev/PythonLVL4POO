class Usuario:
    def __init__(self,nombre= None, pertenencia = False):
        self.nombre = nombre
        self.pertenencia = pertenencia
        self.cantidad = 1 if self.pertenencia else 0
    def tomardef(self,tomar):
        self.cantidad += tomar
        self.pertenencia = True if self.cantidad>=1 else False
    def devolverdef(self,devolver):
        self.cantidad-=devolver
        self.pertenencia = False if self.cantidad == 0 else True
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Posesion: ",self.pertenencia)
        print("Cantidad: ",self.cantidad)

class Biblioteca:
    def __init__(self):
        self.usuario1 = Usuario("Richard",False)
    def operador(self):
        self.usuario1.tomardef(2)
        self.usuario1.devolverdef(2)
    def imprimir(self):
        self.usuario1.imprimir()
