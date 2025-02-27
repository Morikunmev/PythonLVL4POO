class Jugador:
    def __init__(self,nombre,puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
    def __str__(self):
        cadena = f"Nombre del jugador: {self.nombre},rango del jugador:  "
        if self.puntaje<1000:
            cadena+="Principiante"
            return cadena
        else:
            cadena+="Experto"
            return cadena
jugador1 = Jugador("Ana",700)
jugador2 = Jugador("Juan",2000)

print(jugador1)
print(jugador2)