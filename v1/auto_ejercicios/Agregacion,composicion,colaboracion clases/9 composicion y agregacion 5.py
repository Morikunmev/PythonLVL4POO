from mod2 import val3

class Juego:
    def __init__(self,NombreJuego = None,VersionJuego = None,TipoJuego = None):
        self.nombre = val3.ValidarNombre(NombreJuego)
        self.version = val3.ValidarVersion(VersionJuego)
        self.tipo = val3.ValidarTipo(TipoJuego)

class Luchador:
    def __init__(self,NombreLuchador = None,Fuerza = None, Destreza = None, Resistencia = None, Velocidad = None,Tecnica = None):
        self.nombre = val3.ValidarNombre(NombreLuchador)
        self.fuerza = val3.ValidarFuerza(Fuerza)
        self.destreza = val3.ValidarDestreza(Destreza)
        self.resistencia = val3.ValidarResistencia(Resistencia)
        self.velocidad = val3.ValidarVelocidad(Velocidad)
        self.tecnica = val3.ValidarTecnica(Tecnica)

class Escenario:
    def __init__(self):
