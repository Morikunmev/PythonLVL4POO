from Validacion import generaldef
class Operario:
    def __init__(self):
        self.nombre = generaldef.string_nombre("Ingrese el nombre del operario: ")
        self.edad = generaldef.edaddef("Ingrese la edad del operario: ")
        self.horas_trabajadas=generaldef.enterodef("Ingrese las horas trabajadas: ")
        self.valor_hora=generaldef.enterodef("Ingrese cuanto se le paga por hora: ")
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Horas trabajadas: ",self.horas_trabajadas)
        print("Valor hora: ",self.valor_hora)
    def calculo(self):
        sueldo = self.horas_trabajadas * self.valor_hora
        print(f"El sueldo del operario {self.nombre} es {sueldo}")
operario1 = Operario()
operario1.imprimir()
operario1.calculo()
