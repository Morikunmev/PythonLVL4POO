class Alumno:
    def __init__(self,nombre = None, edad = None, nota = None):
        self.nombre = nombre
        self.edad = "mayor de edad" if edad is not None and int(edad)>=18 else("menor de edad" if edad is not None and int(edad)<18 else None)
        self.nota = "Aprobado" if nota is not None and float(nota)>=4.0 else ("Reprobado" if nota is not None and int(nota)<4.0 else None)

alumno1 = Alumno()
print(alumno1.nombre)
print(alumno1.edad)
print(alumno1.nota)