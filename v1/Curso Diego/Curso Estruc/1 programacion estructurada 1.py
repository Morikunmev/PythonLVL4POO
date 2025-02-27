def validar():
    while True:
        try:
            edad = int(input("Ingresa la edad de la persona: "))
            return edad
        except ValueError:
            continue
def nombredef():
    while True:
        nombre = input(f"Ingrese el nombre de persona {registro}: ")
        if nombre.isnumeric() or any(i.isnumeric() for i in nombre) or not nombre.isalpha() or nombre.count(" ")>=1:
            continue
        return nombre.capitalize()

registro=0
while True:
    registro+=1
    print(f"Registro nro: {registro}")
    
    nombre = nombredef()
    edad = validar()
    print(nombre)
    print(edad)
