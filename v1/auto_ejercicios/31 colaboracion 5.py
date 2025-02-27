class Personaje:
    def __init__(self,NombrePersonaje = None,NombreActor = None, participar = False):
        self.NombrePersonaje = NombrePersonaje
        self.NombreActor1 = NombreActor
        self.participar = participar
        self.escenas = 1 if self.participar else 0

    def imprimir(self):
        print("Nombre de Personaje: ",self.NombrePersonaje)
        print("Nombre de Actor: ",self.NombreActor1)
        print("Participara: ", self.participar)
        print("Escenas que rodara: ", self.escenas)
class Actor:
    def __init__(self, jaaj = None):
        self.NombreActor = jaaj.NombreActor1


personaje1 = Personaje("","xd")
personaje1.imprimir()
actor1 = Actor(personaje1)
print(actor1.NombreActor)
