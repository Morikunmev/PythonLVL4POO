from mod2 import val2
class Actor:
    def __init__(self,NombreActor = None,RutActor = None,NacionalidadActor =None):
        self.nombre = val2.ValidarNombre(NombreActor)
        self.rut = val2.ValidarRut(RutActor)
        self.nacionalidad = val2.ValidarNacionalidad(NacionalidadActor)
    def __str__(self, Personaje = None):
        return f"El actor {self.nombre} de rut {self.rut} de nacionalidad {self.nacionalidad} interpretara a {Personaje}"

class Personaje:
    def __init__(self,NombrePersonaje = None, GeneroPersonaje =None):
        self.nombre = val2.ValidadNombrePersonaje(NombrePersonaje)
        self.genero = val2.ValidarGenero(GeneroPersonaje)
    def __str__(self, Actor = None):
        return f"El personaje {self.nombre} de genero {self.genero} sera interpretado por el actor {Actor}"

class Pelicula:
    def __init__(self,NombrePelicula = None,GeneroPelicula = None,FechaEmision = None, FasePelicula = None):
        self.nombre = val2.ValidarNombrePelicula(NombrePelicula)
        self.genero = val2.GeneroPelicula(GeneroPelicula)
        self.fecha = val2.ValidarFecha(FechaEmision)
        self.fase = val2.ValidarFase(FasePelicula)

    def __str__(self,director = None):
        return f"La perlicula {self.nombre} de genero {self.genero} con fecha {self.fecha} dentro de la fase {self.fase} sera dirigida por el director {director}"


class Director:
    def __init__(self, NombreDirector = None, GeneroDirector = None):
        self.nombre = val2.ValidarNombreDirector(NombreDirector)
        self.genero = val2.ValidarGenero(GeneroDirector)

    def __str__(self,NombrePelicula = None):
        return f"El director {self.nombre} de genero {self.genero} Dirigira la pelicula {NombrePelicula}"

actor1 = Actor("Ricky Martin",192222223,"Rusia")
personaje1 = Personaje("Huason","f")
pelicula1 = Pelicula("Spyder Man","f",2009,3)
director1 = Director("","f")

print(actor1.__str__(personaje1.nombre))