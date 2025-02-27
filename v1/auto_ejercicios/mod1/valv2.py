

def nombre23(nombre):
    nombre = f"nombre: {nombre}" if nombre is not None and (not nombre.isnumeric() and not any(i.isnumeric() for i in nombre)) else None
    return nombre

def edad23(edad):
    edad = f"Edad: {edad}" if edad is not None and str(edad).isnumeric() and 12 <= int(edad) <= 20 else None
    return edad
def validacion23(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def sueldo23(sueldo):
    sueldo = f"Sueldo: {sueldo*1.20}" if sueldo is not None and validacion23(sueldo) else None
    return sueldo