import inspect


def ValidarNombre(nombre):
    return "No se han ingresado datos" if nombre is None or str(nombre).isnumeric() or any(i.isnumeric() for i in nombre) else nombre.capitalize()
def ValidarEdad(a):
    return "No se han ingresado datos" if a is None or not str(a).isnumeric() else int(a)
def ValidadGrado(a):
    return "No se han ingresado datos" if a is None or not str(a).isnumeric() else int(a)

def ValidacionNombreCurso(a):
    return "No se han ingresado datos" if a is None or str(a).isnumeric() or any(i.isnumeric() for i in a) else a.capitalize()
def ValidarSeccion(a):
    return "No se han ingresado datos" if a is None or not str(a).isnumeric() else int(a)
def ValidarGeneracion(a):
    return "No se han ingresado datos" if a is None or not str(a).isnumeric() else int(a)

def ValidarTipo(a):
    return "No se han ingresado datos" if a is None or not a in ["publica","privada"] else a.capitalize()

def ValidarEntero(a):
    return "No se han ingresado datos" if a is None or not str(a).isnumeric() else int(a)


