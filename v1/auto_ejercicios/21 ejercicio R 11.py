class Alumno:
    def __init__(self,nombre = None, nota1 = None, nota2 = None, nota3 = None,edad = None):
        self.nombre = nombre
        self.nota1 = float(nota1) if nota1 is not None and 0<=float(nota1) else None
        self.nota2 = float(nota2) if nota2 is not None and 0<=float(nota2) else None
        self.nota3 = float(nota3) if nota3 is not None and 0<=float(nota3) else None
        self.edad = int(edad) if edad is not None and 12<=int(edad)<=20 else None
    def calculo(self):
        if None not in (self.nota1,self.nota2, self.nota3):
            suma = self.nota1 + self.nota2 + self.nota3
            print(suma/3)
        else:
            print("Faltan notas")
alumno1 = Alumno()
print(alumno1.nota1)
print(alumno1.nota2)
print(alumno1.nota3)
alumno1.calculo()