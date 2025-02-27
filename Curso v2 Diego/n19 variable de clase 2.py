class Jugador:
    tiempo = 30
    def __init__(self,nombre,puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
    def imprimir(self):
        print("Noombre: ",self.nombre)
        print("Puntaje: ",self.puntaje)
        print("Fin de juego en ",Jugador.tiempo)
    def pasar_minuto(self):
        Jugador.tiempo-=1
jugador1 = Jugador("richard",100)
jugador2 = Jugador("Juan",50)
while Jugador.tiempo>0:
    jugador1.imprimir()
    jugador2.imprimir()
    jugador1.pasar_minuto()