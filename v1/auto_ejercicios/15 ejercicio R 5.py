from mod1 import operaciones

class Pelicula:
    contador=0
    ListaNombre = []
    listaDuracion = []
    ListaAño = []
    def __init__(self,nombre,duracion,año):
        self.nombre = nombre
        self.duracion = duracion
        self.año = año

        Pelicula.contador+=1
        Pelicula.ListaNombre.append(self.nombre)
        Pelicula.listaDuracion.append(self.duracion)
        Pelicula.ListaAño.append(self.año)
    def __str__(self):
        return f"Nombre: {self.nombre}, Duración: {self.duracion} minutos, Año: {self.año}"

pelicula1 = Pelicula("Spider man",120,1998)
pelicula2 = Pelicula("Soy bajan",30, 1966)

print(f"Se han creado {Pelicula.contador} peliculas")
print(f"Lista de nombres: {Pelicula.ListaNombre}")
print(f"Lista duracion: {Pelicula.listaDuracion}")
print(f"Lista año: {Pelicula.ListaAño}")