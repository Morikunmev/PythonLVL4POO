class Estudiante:

    def __init__(self,nombre = None, edad = None):
        self.nombre = "nombre desconocido" if nombre is None else nombre.capitalize()
        self.edad = "edad desconocida" if edad is None else edad

    def imprimir_estudiante(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
    def agregar_carrera(self,nombre = None,año = None):
        self.asignatura = Carrera(nombre,año)
    def agregar_curso(self,nombre):
        self.asignatura.cursos(nombre)
    def imprimir_general(self):
        self.asignatura.imprimir_carrera()

class Carrera:
    ListaCursos = []
    def __init__(self,nombre = None,año = 1):
        self.nombre = "no agregada" if nombre is None else nombre
        self.año = año

        Universidad.Asignaturas.append(self.nombre)

        Carrera.ListaCursos.clear()
    def cursos(self,nombre_curso):
        Carrera.ListaCursos.append(nombre_curso)
        Universidad.Cursos.append(nombre_curso)

    def imprimir_carrera(self):
        print("Nombre de la carrera: ",self.nombre)
        print("Año del estudiante: ",self.año)
        print("Todos los cursos:")
        for i, valor in enumerate(Carrera.ListaCursos):
            print(f"{i+1}: {valor}")
class Universidad:
    Asignaturas = []
    Cursos = []
    TodosEstudiantes = []
    TodosEdad = []
    def __init__(self,nombre):
        self.nombre = nombre



estudiante1 = Estudiante("richard",24)
estudiante1.agregar_carrera("informatica",2)
estudiante1.agregar_curso("calculo 1")
estudiante1.agregar_curso("programacion 1")
estudiante1.agregar_curso("funciones y matrices")
estudiante1.imprimir_general()
print()
estudiante2 = Estudiante("Juan",21)
estudiante2.agregar_carrera("Pedagojia en ingles",1)
estudiante2.agregar_curso("historia del ingles")
estudiante2.agregar_curso("gramatica")
estudiante2.agregar_curso("cultura")
estudiante2.imprimir_general()
print()
print(Universidad.Cursos)





