class Juego:
    def __init__(self,nombre = None,tipo = None):
        self.nombre = nombre
        self.tipo = "Accion" if tipo is not None else "Accion"
    def Verbo(self):
        print(F"Iniciando Juego: {self.nombre} de tipo {self.tipo}")

class Personaje:
    contador = 0
    def __init__(self,nombre = None,especial = False):
        self.nombre = nombre
        self.especial = True if especial in ["s","si"] else False
        Personaje.contador+=1
    def Imprimir(self,a):
        print(f"Campeon nro {Personaje.contador} de {a}")
        print("Nombre: ",self.nombre)
        print("Tecnicas Especiales: ",self.especial)
class Enfrentamiento:
    def __init__(self, nombre = None, capacidad = 2):
        self.nombre = nombre
        self.capacidad = 2 if capacidad is not None else 2
    def Duelo(self,a,b):
        print(a, "VS", b,"en ",self.nombre)

juego1 = Juego("Streat Fighter")
juego1.Verbo()
personaje1 = Personaje("Goku")
personaje1.Imprimir(juego1.nombre)
personaje2 = Personaje("Saitama")
personaje2.Imprimir(juego1.nombre)

arena1 = Enfrentamiento("Tierra del Fuego")
arena1.Duelo(personaje1.nombre,personaje2.nombre)