class Jugador:
    Minutos = 30
    def __init__(self,nombre,puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
    def Imprimir(self):
        print("Nombre: ",self.nombre)
        print("Puntaje: ",self.puntaje)
        print("Fin de juego en: ",Jugador.Minutos)
    def pasar_minutos(self):
        Jugador.Minutos -=1
jugador1 = Jugador("Ana",100)
jugador2 = Jugador("Juan",50)
while Jugador.Minutos>0:
    jugador1.Imprimir()
    jugador2.Imprimir()
    jugador1.pasar_minutos()