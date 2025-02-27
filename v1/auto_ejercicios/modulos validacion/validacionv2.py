def nombredef(nombre):
    nombre = f"Nombre: {nombre.capitalize()}" if nombre is not None and (not nombre.isnumeric() and not any(i.isnumeric() for i in nombre)) else None
    return nombre

def edaddef(edad):
    edad = f"Edad: {edad}" if edad is not None and str(edad).isnumeric() and 12<=int(edad)<=20 else None
    return edad

def flotantedef(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def alturadef(altura):
    if altura is not None and str(altura).isnumeric() and flotantedef(altura) and altura>=1.80:
        return "Mucha altura"
    elif altura is not None and flotantedef(altura) and 1.60<=altura<=1.79:
        return "Media Altura"
    elif altura is not None and flotantedef(altura) and 1.60<altura:
        return "baja altura"
    else:
        return None




