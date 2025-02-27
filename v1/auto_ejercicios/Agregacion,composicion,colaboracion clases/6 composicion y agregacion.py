class Estudiante:
    ListaEstudiante = []
    ListaEdad = []
    ListaCurso = []
    def __init__(self,NombreEstudiante = None,EdadEstudiante = None,AñoCurso = None):
        self.nombre = "No se han ingresado datos" if NombreEstudiante is None or str(NombreEstudiante).isnumeric() or any(i.isnumeric() for i in NombreEstudiante) else NombreEstudiante.capitalize()
        self.edad = "No se han ingresado datos" if EdadEstudiante is None or not str(EdadEstudiante).isnumeric() else EdadEstudiante
        self.curso = "No se han ingresado datos" if AñoCurso is None or not str(AñoCurso).isnumeric() else AñoCurso

        Estudiante.ListaEstudiante.append(self.nombre)
        Estudiante.ListaEdad.append(self.edad)
        Estudiante.ListaCurso.append(self.curso)
    def VerboEstudiante(self, a = None):
        print(f"El estudiante llamado {self.nombre} de edad {self.edad} años cursa en {self.curso} grado en el curso {a}")

    def DatosEstudiante(self):
        for i in range(len(Estudiante.ListaEstudiante)):
            print(f"Registro nro {i+1}: {Estudiante.ListaEstudiante[i]}")
class Curso:
    ListaCurso = []
    ListaSeccion = []
    def __init__(self,NombreCurso = None, SeccionCurso = None):
        self.nombre = "No se han ingresado datos" if NombreCurso is None or str(NombreCurso).isnumeric() or any(i.isnumeric() for i in NombreCurso) else NombreCurso.capitalize()
        self.seccion = "No se han ingresado datos" if SeccionCurso is None or not str(SeccionCurso).isnumeric() else SeccionCurso

        Curso.ListaCurso.append(self.nombre)
        Curso.ListaSeccion.append(self.seccion)

    def VerboCurso(self,a =None):
        print(f"El curso {self.nombre} de la seccion {self.seccion} es cursado por {a}")

    def DatosCurso(self):
        print("Todos los cursos impartidos")
        for i in range(len(Curso.ListaCurso)):
            print(f"Registro nro {i+1}: {Curso.ListaCurso[i]}, Seccion: {Curso.ListaSeccion[i]}")
class Universidad:
    def __init__(self,NombreUniversidad = None, TipoUniversidad = None):
        self.nombre = "No se han ingresado datos" if NombreUniversidad is None or str(NombreUniversidad).isnumeric() or any(i.isnumeric() for i in NombreUniversidad) else NombreUniversidad.capitalize()
        self.tipo = "No se han ingresado datos" if TipoUniversidad is None or not TipoUniversidad in ["publica","privada"] else TipoUniversidad.capitalize()

    def VerboUniversidad(self,a):
        print(f"El señor/a {a} estudia en: {self.nombre} de tipo: {self.tipo}")

#Creacion de objetos de la clase estudiante
estudiante1 = Estudiante("Richard",24,1)
estudiante2 = Estudiante("Skarlett",22,2)
estudiante3 = Estudiante("Juan",24,6)
estudiante4 = Estudiante("Alberto",26,2)

#Creacion de objetos de la clase curso
curso1 = Curso("Programacion")
curso2 = Curso("Turismo")
curso3 = Curso("Administracion")

#Creacion de objetos de la clase Universidad
universidad1 = Universidad("Universidad de Magallanes","publica")
universidad2 = Universidad("Inacap","privada")
universidad3 = Universidad("Santo tomas","privada")

#acciones/metodo
estudiante1.VerboEstudiante(curso1.nombre)
estudiante2.VerboEstudiante(curso2.nombre)
estudiante3.VerboEstudiante(curso2.nombre)