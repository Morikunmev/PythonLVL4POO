class Persona:
    def __init__(self):
        self.nombre = input("Ingrese nombre: ")
        self.edad = int(input("Ingrese la edad: "))
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese sueldo"))
    def imprimir(self):
        super().imprimir()
        print(f"Sueldo: {self.sueldo}")
    def paga_impuestos(self):
        if self.sueldo>3000:
            print(self.nombre,"debe pagar impuestos")
        else:
            print(self.nombre,"no paga impuestos")


empleado1 = Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()