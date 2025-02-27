class Personaje:
    def __init__(self,nombre = None):
        self.nombre = nombre
    def imprimir(self):
        print("Personaje: ",self.nombre)
class Codigo:
    def __init__(self,lenguaje = None):
        self.lenguaje = lenguaje
    def procesar(self):
        print(f"Procesando en codigo {self.lenguaje}")

class Juego:
    def __init__(self,nombre = None,tipo = "Accion"):
        self.nombre = nombre
        self.tipo = "Accion" if tipo is not None else "Accion"
        self.codigo = Codigo("Python")
    def EncenderJuego(self):
        print(f"Iniciando el juego {self.nombre} de tipo {self.tipo}")
        self.codigo.procesar()

    def Agregacion(self):
        print("Personajes")
        self.personaje1 = Personaje("Goku")
        self.personaje2 = Personaje("Naruto")

        self.personaje1.imprimir()
        self.personaje2.imprimir()




juego1 = Juego("Streat Fighter")
juego1.EncenderJuego()
juego1.Agregacion()
