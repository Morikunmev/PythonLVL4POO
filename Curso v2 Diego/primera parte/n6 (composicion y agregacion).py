#Agregacion
class Salario:
    def __init__(self,monto):
        self.monto = monto
    def salarioAnual(self):
        return (self.monto * 12)
class Empleado:
    def __init__(self,nombre,edad,monto):
        self.nombre = nombre
        self.edad = edad
        self.salario = monto
    def salarioEmpleado(self):
        return self.salario.salarioAnual()
salario =Salario(250000)
empleado = Empleado("richard",24,salario)
print(empleado.salarioEmpleado())
del(empleado)
print(salario.monto)