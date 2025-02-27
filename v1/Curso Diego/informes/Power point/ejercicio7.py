class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)
    def __init__(self,titulo=None,duracion = None, lanzamiento = None):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)
    def __del__(self):
        if self.titulo == "El padrino":
            print("Se esta borrando la pelicula",self.titulo)
        else:
            print("No se esta eliminando nada")
    def imprimir(self):
        print("Titulo: ",self.titulo)
        print("Duracion, ",self.duracion)
        print("Lanzamiento, ",self.lanzamiento)

pelicula1 = Pelicula("El padrino",175,1972)
pelicula2 = Pelicula("Magia",120,1999)
pelicula3=Pelicula()


