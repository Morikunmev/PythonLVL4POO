def ValidarNombre(a):
    return "Nombre: Str" if a is None or str(a).isnumeric() or any(i.isnumeric() for i in a) else a.capitalize()
def ValidarRut(a):
    return "Rut: Int" if a is None or not str(a).isnumeric() or len(str(a)) !=9 else int(a)

def ValidarNacionalidad(a):
    return "Nacionalidad: Str" if a is None or str(a).isnumeric() or any(i.isnumeric() for i in a) else a.capitalize()

def ValidadNombrePersonaje(a):
    return "Nombre: str" if a is None else a.capitalize()
def ValidarGenero(a):
    return "Genero: str" if a is None or not str(a) in ["f","m"] else str(a).capitalize()
def ValidarNombrePelicula(a):
    return "Nombre Pelicula: Str" if a is None else str(a).capitalize()

def GeneroPelicula(a):
    return "Genero Pelicula: Str" if a is None or not str(a) in ["accion","fantasia","ciencia ficcion"] else str(a).capitalize()
def ValidarFecha(a):
    return "Fecha Pelicula : Int" if a is None or str(a).isalpha() or not 2008<= int(a)<=2020 else int(a)

def ValidarFase(a):
    return "Fase Pelicula: Int" if a is None or str(a).isalpha() or not 1<= int(a)<=3 else int(a)

def ValidarNombreDirector(a):
    return "Nombre Director: Str" if a is None or str(a).isnumeric() or any(i.isnumeric() for i in a) else str(a).capitalize()