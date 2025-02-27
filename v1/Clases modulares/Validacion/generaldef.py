def string_nombre(mensaje):
    while True:
        nombre = input(mensaje)
        if nombre.isnumeric() or any(i.isnumeric() for i in nombre) or len(nombre) < 3 or len(nombre.split())>1 or not any(i.isalpha() for i in nombre):
            continue
        return nombre.capitalize()
    
nombre_valido = string_nombre("Por favor, ingrese su nombre: ")

print("Nombre válido:", nombre_valido)


def enterodef(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero <= 0:
                continue
            return numero
        except ValueError:
            continue


def entero1def(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            continue


def edaddef(mensaje):
    while True:
        try:
            edad = int(input(mensaje))
            if not 1 <= edad <= 150:
                continue
            return edad
        except ValueError:
            continue


def preciodef(mensaje):
    while True:
        try:
            precio = float(input(mensaje))
            if precio <= 0:
                continue
            return precio
        except ValueError:
            continue


# Definicion de genero
def generodef(mensaje):
    while True:
        genero = input(mensaje).upper()
        if genero in ["F", "M"]:
            return genero


# Definicion de genero de Pelicula
def pelicula_genero(mensaje):
    while True:
        genero = input(mensaje).lower()
        if genero in ["accion", "fantasia", "ficcion"]:
            genero = ["accion", "fantasia", "ficcion"]
            return genero


# Definicion de fase
def fasedef(mensaje):
    while True:
        try:
            fase = int(input(mensaje))
            if 1 <= fase <= 3:
                return fase
        except ValueError:
            continue


# Definicion de año
def añodef(mensaje):
    while True:
        try:
            año = int(input(mensaje))
            if 2008 <= año <= 2020:
                return año
        except ValueError:
            continue


# Definicion estudio
def estudiodef(mensaje):
    while True:
        try:
            estudio = input(mensaje).capitalize()
            if estudio == "Marvel":
                return estudio
        except ValueError:
            continue
