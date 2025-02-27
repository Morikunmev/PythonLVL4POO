from Validacion import generaldef

class Persona:
    def __init__(self):
        self.nombre=generaldef.string_nombre("Ingrese el nombre de la persona: ")
        self.edad = generaldef.edaddef("Ingrese la edad de la persona: ")
        self.sueldo=generaldef.preciodef(f"Ingrese el sueldo de {self.nombre}: ")
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Sueldo: ",self.sueldo)
    def condicional(self):
        if self.sueldo>3000:
            print("Esta persona debe pagar impuestos")
        else:
            print("No debe pagar impuestos")
persona1 = Persona()
persona1.imprimir()
persona1.condicional()
        
