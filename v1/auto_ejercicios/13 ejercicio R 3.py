class Alumno:
    def __init__(self, nombre,nota1,nota2,nota3):
        self.nombre = nombre
        self.nota1=nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def calculo(self):
        suma = self.nota1 + self.nota2 + self.nota3
        self.promedio = suma / 3
    def __str__(self):
        return f"El promedio es {self.promedio}"

alumno1=Alumno("Richard",5.0,4.0,3.0)
alumno1.calculo()
print(alumno1)