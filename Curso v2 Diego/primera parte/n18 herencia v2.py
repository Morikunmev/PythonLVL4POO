class Persona:
    def __init__(self,nombre,edad,DNI):
        self.nombre = nombre
        self.edad = edad
        self.dni = DNI
    def presentarse(self):
        print(f"Hola! me llamo {self.nombre} y tengo {self.edad} años")
class Trabajador(Persona):
    def __init__(self,nombre,edad,DNI, sueldo, cargo, empresa):
        super().__init__(nombre,edad,DNI)
        self.sueldo =sueldo
        self.cargo = cargo
        self.empresa = empresa
    def calcularSueldoAnual(self):
        return 12*self.sueldo + 2000

class Estudiante(Persona):
    def __init__(self,nombre,edad, DNI,universidad, curso,asignatura):
        super().__init__(nombre,edad, DNI)
        self.universidad = universidad
        self.curso =curso
        self.asignatura = asignatura
    def describirse(self):
        print(f"Hola soy {self.nombre}!. Tengo {self.edad} y estudio en la universidad {self.universidad}")

trabajador1 = Trabajador("Juan",24,"eqwewq",1500,"machaca","google")
trabajador1.presentarse()
print(trabajador1.calcularSueldoAnual())

estudiante1 = Estudiante("Maria",20,"12312321k","Universidad de madrid",3, ["programacion","calculo","algebra"])
estudiante1.describirse()