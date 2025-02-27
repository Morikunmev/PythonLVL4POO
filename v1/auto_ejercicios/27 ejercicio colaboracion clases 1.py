class Estadio:
    def __init__(self, nombre=None):
        self.nombre = nombre

    def imprimir(self):
        print(self.nombre)

class Jugador:
    contador = 0

    def __init__(self):
        self.jugador1 = Estadio("Richard")
        self.jugador2 = Estadio("Felipe")
        Jugador.contador += 1  # Aumenta el contador cada vez que se crea una instancia de Jugador

    def total(self):
        self.jugador1.imprimir()
        self.jugador2.imprimir()

# Crear instancias de Jugador
jugador1 = Jugador()

# Imprimir el contador de instancias de Jugador
print("Número total de instancias de Jugador:", Jugador.contador)



