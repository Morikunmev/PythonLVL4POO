from mod1 import operacionesv2
lista = ["Accion","Fantasia","Ciencia Ficcion"]
class Pelicula:
    def __init__(self,estudio ="Marvel",nombre = None,genero = lista,año = None,fase = None):
        self.estudio = estudio
        self.nombre = nombre
        self.genero = genero
        self.año = int(año) if str(año).isnumeric() and (2008 <= int(año) <= 2020) else None
        self.fase = int(fase) if str(fase).isnumeric() and (1<=int(fase)<=3) else None

    def datos(self):
        operacionesv2.ejercicio17(self.estudio,self.nombre,self.genero,self.año,self.fase)

pelicula1 = Pelicula()
pelicula1.datos()