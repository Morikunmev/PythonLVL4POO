class Estudiante:
    Largo = 0
    def __init__(self,nombre = None):
        self.nombre = nombre
        self.promedio = 0
        Estudiante.Largo+=1
    def agregar_nota(self,nota):
        self.nota = []
        self.nota.append(nota)
    def calculo_promedio(self):
        self.promedio = sum(self.nota) / len(self.nota)
    def retornar_promedio(self):
        return self.promedio
    def imprimir(self):
        print(f"{self.nombre} tiene promedio: {self.promedio}")

class Curso:
    def __init__(self):
        self.estudiante1 = Estudiante("richard")
        self.estudiante2 = Estudiante("pablo")
        self.estudiante3 = Estudiante("noe")
    def operar(self):
        self.estudiante1.agregar_nota(7.0)
        self.estudiante1.agregar_nota(3.0)
        self.estudiante1.agregar_nota(4.0)
        self.estudiante1.agregar_nota(5.0)

        self.estudiante2.agregar_nota(3.0)
        self.estudiante2.agregar_nota(5.0)
        self.estudiante2.agregar_nota(4.0)
        self.estudiante2.agregar_nota(7.0)
        self.estudiante2.agregar_nota(4.0)

        self.estudiante3.agregar_nota(4.0)
        self.estudiante3.agregar_nota(2.0)
        self.estudiante3.agregar_nota(1.0)
        self.estudiante3.agregar_nota(4.0)

        self.estudiante1.calculo_promedio()
        self.estudiante2.calculo_promedio()
        self.estudiante3.calculo_promedio()
    def promedio_total(self):
        total = (self.estudiante1.retornar_promedio() + self.estudiante2.retornar_promedio() + self.estudiante3.retornar_promedio()) / Estudiante.Largo
        print("El promedio total de los estudiantes es: ",total)
        self.estudiante1.imprimir()
        self.estudiante2.imprimir()
        self.estudiante3.imprimir()
curso1 = Curso()
curso1.operar()
curso1.promedio_total()


