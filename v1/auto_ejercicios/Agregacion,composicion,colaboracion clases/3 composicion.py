class Codigo:
    def __init__(self,codigo):
        self.codigo = codigo
    def Procesar(self):
        print(f"Procesando el codigo en {self.codigo}")
class Personaje:
    def __init__(self,nombre = None,a = None,b = None,c = None,d = False):
        self.nombre = nombre
        self.a = a
        self.b = b
        self.c = c
        self.d = True if d in ["s","si"] else False
    def VerboPersonaje(self):
        print(f"Estadisticas de {self.nombre}: ")
        print(self.a)
        print(self.b)
        print(self.c)
        print("Tecnicas Especiales: ",self.d)
    def MensajePersonaje(self):
        print("Añadiendo Personajes")
class Juego:
    def __init__(self,nombre =None, tipo = None):
        self.nombre = nombre
        self.tipo = "accion" if tipo is not None else "accion"
        self.codigo = Codigo("Python")

    def AñadiendoPersonajes(self):
        self.personaje1 = Personaje("Goku")
        self.personaje2 = Personaje("Saitama")

    def encender(self):
        print(f"Iniciando juego {self.nombre} de tipo {self.tipo}")
        self.codigo.Procesar()
        self.personaje1.MensajePersonaje()
    def EstadisticasPersonajes(self):
        self.personaje1.VerboPersonaje()
        self.personaje2.VerboPersonaje()

class Escenario:
    def __init__(self, NombreEscenario, CapacidadEscenario=2):
        self.nombre = NombreEscenario
        self.capacidad = 2 if CapacidadEscenario is not None else 2

    def Enfrentamiento(self, personaje1 =None, personaje2=None):
        print(f"Duelo 1: {personaje1} vs {personaje2}")

    def VerboEscenario(self):
        print("Luchan solo y solo 2 Jugadores")



juego1 = Juego("Naruto strom 4")
juego1.AñadiendoPersonajes()
juego1.encender()
juego1.EstadisticasPersonajes()
escenario1 = Escenario("Desierto")
escenario1.VerboEscenario()
escenario1.Enfrentamiento("Goku")
