def validar():
    while True:
        try:
            nombre = input("Ingrese nombre: ")
            if nombre.isnumeric() or any(i.isnumeric() for i in nombre) or not nombre.isalpha() or nombre.count(" ")>=1:
                continue
            return nombre.capitalize()
        except ValueError:
            continue
def validar1():
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad <= 0 or not 1<=edad<=100:
                continue
            return edad
        except ValueError:
            continue

class Persona:
    def datos(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
    def mayor(self):
        if self.edad >=18:
            print(self.nombre, "Es mayor de edad")
        else:
            print(self.nombre, "es menor de edad")
        
persona1 = Persona()
persona1.datos(validar(),validar1())
persona1.imprimir()
persona1.mayor()
