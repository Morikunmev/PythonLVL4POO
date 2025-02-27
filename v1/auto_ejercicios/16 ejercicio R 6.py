from mod1 import operaciones
class Juego:
    ContadorJuego = 0
    ListaNombre = []
    ListaVersion = []

    def __init__(self,nombre,version):
        self.nombre = nombre
        self.version = version

        Juego.ContadorJuego+=1
        Juego.ListaNombre.append(self.nombre)
        Juego.ListaVersion.append(self.version)
    def DatosInstancia(self):
        operaciones.DatosJuego(self.nombre,self.version)
class Luchador:
    ContadorNombre = 0
    ListaNombre = []
    ListaPromedio = []
    def __init__(self,nombre = None, fuerza = 0,destreza = 0, resistencia = 0, velocidad = 0):
        self.nombre = nombre
        self.fuerza = fuerza
        self.destreza = destreza
        self.resistencia = resistencia
        self.velocidad = velocidad
        Luchador.ContadorNombre+=1
        Luchador.ListaNombre.append(self.nombre)
        Luchador.ListaPromedio.append(operaciones.promediodef(fuerza,destreza,resistencia,velocidad))

    def DatosInstancia(self):
        operaciones.Estadisticas(self.nombre,self.fuerza,self.destreza,self.resistencia,self.velocidad)


class General:
    def IteracionJuegodef(self):
        operaciones.IteracionJuego(Juego)
    def IteracionLuchadordef(self):
        operaciones.IteracionLuchador(Luchador)
    def mayordef(self):
        operaciones.mayorpromediodef(Luchador)
    def menordef(self):
        operaciones.menorpromediodef(Luchador)


juego1 = Juego("Stret Fighter","Nueva Version")
juego1.DatosInstancia()
print()
luchador1= Luchador("Richard",5,6,1,9)
luchador2= Luchador("Felipe",10,0,1,10)
general1 =General()
general1.IteracionLuchadordef()