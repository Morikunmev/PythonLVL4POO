class Empleado:
    def __init__(self,nombre = None, sueldo = None):
        self.nombre = nombre
        self.sueldo = "debe pagar impuestos" if sueldo is not None and int(sueldo)>=3000 else ("No debe pagar impuesto" if sueldo is not None and int(sueldo)<3000 else None)
empleado1 = Empleado("Richard",33333.2)
print(empleado1.nombre)
print(empleado1.sueldo)