from mod2 import val1
class Estudiante:
    def __init__(self, NombreEstudiante = None, EdadEstudiante = None, GradoEstudiante = None):
        self.nombre = val1.ValidarNombre(NombreEstudiante)
        self.edad = val1.ValidarEdad(EdadEstudiante)
        self.grado = val1.ValidadGrado(GradoEstudiante)
    def VerboEstudiante(self,NombreCarrera = None):
        print(f"El/la estudiante {self.nombre} de {self.edad} años de edad cursa en {self.grado} grado de la carrera de {NombreCarrera}")

class Curso:
    def __init__(self,NombreCurso = None,SeccionCurso = None, GeneracionCurso = None):
        self.nombre = val1.ValidacionNombreCurso(NombreCurso)
        self.seccion = val1.ValidarSeccion(SeccionCurso)
        self.generacion = val1.ValidarGeneracion(GeneracionCurso)

    def VerboCurso(self,NombreAlumno = None):
        print(f"El curso de {self.nombre} de la seccion {self.seccion} de la {self.generacion} generacion es cursada por {NombreAlumno}")

class Universidad:
    def __init__(self,NombreUniversidad = None, TipoUniversidad = None, CantidadEstudiantesUniversidad = None):
        self.nombre = val1.ValidarNombre(NombreUniversidad)
        self.tipo = val1.ValidarTipo(TipoUniversidad)
        self.cantidad = val1.ValidarEntero(CantidadEstudiantesUniversidad)
    def __str__(self,Nombre =None, Curso = None):
        return f"En la {self.nombre} de tipo {self.tipo} con cantidad de {self.cantidad} personas estudia el señor/señora {Nombre} en el curso de {Curso}"
    def Contador(self):
        print(f"{Universidad.contador} ingresados")


estudiante1 = Estudiante("Richard",24,2)
estudiante2 = Estudiante("Felipe",25,1)
estudiante3 = Estudiante("Maria",19,1)
estudiante4 = Estudiante("Carlos",18,3)

curso1 = Curso("Programacion",3312,2023)
curso2 = Curso("Turismo",1222,2019)

universidad1 = Universidad("Universidad de Magallanes","publica",1300)
