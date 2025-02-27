def nombredef():
    while True:
        nombre = input("Ingrese nombre: ")
        if nombre.isnumeric() or any(i.isnumeric() for i in nombre) or not nombre.isalpha() or nombre.count(" ")>=1 or len(nombre)<=4:
            continue
        return nombre.capitalize()
def edaddef():
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            while edad<=0 or not 18<=edad<=100:
                edad=int(input("Ingrese la edad: "))
            sueldo=float(input("Ingrese su sueldo: "))
            while sueldo<=0:
                sueldo=int(input("Ingrese su sueldo: "))
            return edad,sueldo
        except ValueError:
            continue


class Empleado:
    def __init__(self):
        self.nombre = nombredef()
        self.edad,self.sueldo = edaddef()
        
    def imprimir(self):
        print(f"Nombre :{self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sueldo: {self.sueldo}")
        
    def impuestos(self):
        if self.sueldo>=3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")
        
empleado1 = Empleado()
empleado1.imprimir()
empleado1.impuestos()


        
