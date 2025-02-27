class Empleado:
    def __init__(self):
        self.nombre = input("nombre empleado: ")
        self.sueldo = float(input("sueldo empleado: "))
    def imprimir(self):
        print("nombre: ",self.nombre)
        print("sueldo: ",self.sueldo)
    def pagaimpuestos(self):
        if self.sueldo >3000:
            print("debe pagar impuestos")
        else:
            print("no paga impuestos")
empleado1 = Empleado()
empleado1.imprimir()
empleado1.pagaimpuestos()