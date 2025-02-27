class Salario:
    def __init__(self,monto):
        self.monto = monto
    def salarioAnual(self):
        return self.monto * 12
class Empleado:
    def __init__(self,nombre, edad, monto):
        self.nombre = nombre
        self.edad = edad
        self.salario = Salario(monto)
    def salarioEmpleado(self):
        return self.salario.salarioAnual()
empleado = Empleado("richard",24,250000)
print(empleado.salario.salarioAnual())