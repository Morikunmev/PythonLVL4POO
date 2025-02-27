class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)

    def __del__(self):
        print("Se esta borrando la pelicula",self.titulo)


pelicula1 = Pelicula("El padrino",175,1972)
pelicula1=Pelicula("Volver al futuro",125,1982)
