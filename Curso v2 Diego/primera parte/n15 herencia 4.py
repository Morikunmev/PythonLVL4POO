class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def acciones(self):
        print(self.nombre,"camina")
        print(self.nombre,"corre")
class Profesor(Persona):
    def __init__(self,nombre,edad,años_experiencia):
        super().__init__(nombre,edad)
        self.años_experiencia = años_experiencia
    def acciones(self):
        super().acciones()
        print(f"El profesor tiene {self.años_experiencia} años de experiencia")
class Estudiante(Persona):
    def __init__(self,nombre,edad,asignatura,años_curso):
        super().__init__(nombre,edad)
        self.asignatura = asignatura
        self.años_curso = años_curso
    def acciones(self):
        super().acciones()
        print(f"Cursa la asignatura: {self.asignatura}")
        print(f"Esta en {self.años_curso} curso")