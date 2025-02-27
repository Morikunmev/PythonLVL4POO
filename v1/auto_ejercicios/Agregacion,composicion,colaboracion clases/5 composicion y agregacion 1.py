class Autor:
    def __init__(self, NombreAutor = None, RutAutor = None, NacionalidadAutor = None):
        self.nombre = "No se han ingresado datos" if NombreAutor is None or NombreAutor.isnumeric() or any (i.isnumeric() for i in NombreAutor) else NombreAutor.capitalize()
        self.rut = "No se han ingresado datos" if RutAutor is None or not str(RutAutor).isnumeric() or len(str(RutAutor)) != 9  else RutAutor
        self.nacionalidad = "No se han ingresado datos" if NacionalidadAutor is None or NacionalidadAutor.isnumeric() or any(i.isnumeric() for i in NacionalidadAutor) else NacionalidadAutor.capitalize()

    def VerboAutor(self,NombreAutor = None, RutAutor = None, NacionalidadAutor = None, cantidad = None):
        print(f"El escrito llamado {NombreAutor} de rut {RutAutor} de nacionalidad {NacionalidadAutor} escribe {cantidad} libros")


class Libro:
    ContadorIndividual = 0
    ListaTitulos = []
    def __init__(self,NombreLibro = None,IsbnLibro = None):
        self.nombre = "No se han ingresado datos" if NombreLibro is None else NombreLibro.capitalize()
        self.isbn = "No se han ingresado datos" if IsbnLibro is None or not str(IsbnLibro).isnumeric() or len(str(IsbnLibro)) !=12 else IsbnLibro
        Libro.ContadorIndividual+=1
        Libro.ListaTitulos.append(self.nombre)

    def VerboLibro(self,NombreLibro = None, IsbnLibro = None, NombreAutor = None, RutAutor = None, NacionalidadAutor = None):
        print(f"El libro {NombreLibro} de isbn {IsbnLibro} es escrito por {NombreAutor} de rut {RutAutor} de nacionalidad {NacionalidadAutor}")

class Biblioteca:
    def __init__(self,NombreBiblioteca = None,PasajeBiblioteca = None):
        self.nombre = "No se han ingresado datos" if NombreBiblioteca is None or str(NombreBiblioteca).isnumeric() else NombreBiblioteca.capitalize()
        self.pasaje = "No se han ingresado datos" if PasajeBiblioteca is None or str(PasajeBiblioteca).isnumeric() else PasajeBiblioteca.capitalize()

    def Mostrador(self, a = None):
        print("Registro de libros")
        for i in range(len(a)):
            print(f"Registro nro {i+1}: {a[i]}")





autor1 = Autor("Richard",196629246,"Chileno")
libro1 = Libro("Harry Potter",111111111111)
biblioteca1 = Biblioteca("Catedra","Santa Maria")
biblioteca1.Mostrador(libro1.ListaTitulos)
