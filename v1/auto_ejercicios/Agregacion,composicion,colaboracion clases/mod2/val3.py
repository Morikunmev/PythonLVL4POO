def ValidarNombre(a):
    return f"Nombre: str" if a is None else a.capitalize()
def ValidarVersion(a):
    return f"Version: str" if a is None else a.capitalize()

def ValidarTipo(a):
    return f"Tipo: str" if a is None or not str(a) == "juego de batallas" else a.capitalize()

def ValidarFuerza(a):
    return f"Fuerza: int" if a is None or str(a).isnumeric() else int(a)

def ValidarDestreza(a):
    return f"Destreza: int" if a is None or not str(a).isnumeric() else int(a)

def ValidarResistencia(a):
    return f"Resistencia: int" if a is None or not str(a).isnumeric() else int(a)

def ValidarVelocidad(a):
    return f"Velocidad: int" if a is None or str(a).isalpha() else int(a)

def ValidarTecnica(a):
    return f"Tecnicas Especiales: {False}" if a is None else True
