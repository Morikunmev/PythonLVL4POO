def mayoredaddef(edad = None):
    resultado = "mayor de edad" if edad>=18 else "menor de edad"
    return resultado
def datosdef(a,b):
    print("Datos")
    print("Nombre: ",a)
    print("Edad: ",b)
def ejercicio17(a,b,c,d,e):
    print("Datos")
    print("Estudio: ",a)
    print("Nombre: ",b)
    print("Genero: ",c)
    print("Año: ",d)
    print("Fase: ",e)
def ejercicio19(a,b,c,e):
    print(a),print(b),print(c),print(e)

def edad19(edad):
    edaddef = f"mayor de edad: {edad}" if edad is not None and int(edad) >= 18 else (f"menor de edad{edad}" if edad is not None and int(edad) < 18 else None)
    return edaddef
def altura19(altura):
    alturadef = f"Mucha altura: {altura}" if altura is not None and altura>=1.81 else f"Media Altura: {altura}" if altura is not None and 1.80>=altura>=1.60 else f"baja altura: {altura}" if altura is not None and 1.60>(altura) else None
    return alturadef
def valido19(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def sueldo19(sueldo):
    sueldodef = sueldo * 1.10 if sueldo is not None and valido19(sueldo) else None
    sueldodef = round(sueldodef,3)
    return sueldodef