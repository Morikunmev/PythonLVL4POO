class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)

    def __del__(self):
        print("Se esta borrando la pelicula",self.titulo)

    def __str__(self):
        return f"{self.titulo} lanzada en {self.lanzamiento} con una duracion de {self.duracion} minutos"
    def __len__(self):
        return self.duracion


pelicula1 = Pelicula("El padrino",175,1972)
str(pelicula1)
len(pelicula1)