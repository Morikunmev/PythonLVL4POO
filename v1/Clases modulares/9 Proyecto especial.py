from Validacion import generaldef

class Pelicula:
    NombrePelicula=""
    GeneroPelicula=""
    FechaEmision=0
    Estudio=""
    Fase=0
    def __init__(self):
        Pelicula.NombrePelicula = generaldef.string_nombre("Ingresa el nombre de la pelicula (Cualquier nombre): ")
        Pelicula.GeneroPelicula = generaldef.pelicula_genero("Ingresa el genero de la pelicula (accion,fantasia,ficcion): ")
        Pelicula.FechaEmision = generaldef.añodef("Ingresa la fecha de emision (2008-2020): ")
        Pelicula.Estudio = generaldef.estudiodef("Ingresa el estudio (Marvel): ")
        Pelicula.Fase = generaldef.fasedef("Ingresa la fase en que se encuentra (1-3): ")
    def imprimir(self):
        print("Nombre Pelicula: ",Pelicula.NombrePelicula)
        print("Genero Pelicula: ",Pelicula.GeneroPelicula)
        print("Fecha Emision: ",Pelicula.FechaEmision)
        print("Estudio: ",Pelicula.Estudio)
        print("Fase: ",Pelicula.Fase)

pelicula1 = Pelicula()
pelicula1.imprimir()

class Director:
    NombreDirector = ""
    GeneroDirector = ""
    def __init__(self):
        self.NombreDirector = generaldef.string_nombre(f"Ingresa el nombre del director de la pelicula {pelicula1.NombrePelicula}: ")
        self.GeneroDirector = generaldef.generodef(f"Ingrese el genero del director {self.NombreDirector} (F/M): ")
    def imprimir(self):
        print("Nombre Director: ",self.NombreDirector)
        print("Genero Director: ",self.GeneroDirector)
director1 = Director()
director1.imprimir()

class Actor:
    NombreActor=""
    GeneroActor=""
    Nacionalidad=""
    def __init__(self):
        self.NombreActor=generaldef.string_nombre(f"Ingresa el nombre del actor que participara en la pelicula {pelicula1.NombrePelicula}: ")
        self.GeneroActor=generaldef.generodef(f"Ingrese el genero del actor {self.NombreActor} (F,M): ")
        self.Nacionalidad=generaldef.string_nombre(f"Ingrese la nacionalidad del actor {self.NombreActor}: ")
    def imprimir(self):
        print("Nombre Actor: ",self.NombreActor)
        print("Genero Actor: ",self.GeneroActor)
        print("Nacionalidad Actor: ",self.Nacionalidad)

actor1 = Actor()
actor1.imprimir()

class Personaje:
    NombrePersonaje=""
    GeneroPersonaje=""
    def __init__(self,actor):
        self.NombrePersonje=generaldef.string_nombre(f"Ingrese el personaje que interpretara el actor {actor1.NombreActor}: ")
        self.GeneroPersonaje=generaldef.generodef(f"Ingrese el genero del personaje que interpretara el actor {actor1.NombreActor} (F/M): ")
        self.actor=actor
    def imprimir(self):
        print("Nombre Personaje: ", self .NombrePersonje)
        print("Genero Personaje: ", self.GeneroPersonaje)
        print("Actor que lo interpretara: ",self.actor.NombreActor)

personaje1=Personaje(actor1)
personaje1.imprimir()


    
