class Empleado:
    def __init__(self,nombre,sueldoMensual):
        self.nombre = nombre
        self.sueldoMensual = sueldoMensual
    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual * (1 * 1/100)
        print(f"El sueldo anual de {self.nombre}, empleado normal, es de {sueldo} $")
class Contable(Empleado):
    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual * (1 * 4/100)
        print(f"El sueldo anual de {self.nombre}, Contable, es de {sueldo} $")
class Publicista(Empleado):
    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual * (1 * 5/100)
        print(f"El sueldo anual de {self.nombre}, Publicista, es de {sueldo} $")
class Becario(Empleado):
    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual
        print(f"El sueldo anual de {self.nombre}, Publicista, es de {sueldo} $")

empleados = [
    Empleado("Juan",1000),
    Contable("Angela",1100),
    Publicista("Ryan",1200),
    Becario("Pepito",750)
]
for empleado in empleados:
    empleado.calcularSueldoAnual()
