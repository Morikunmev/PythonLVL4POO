#FUNCIONES DE VALIDACION

def validacion():
    while True:
        try:
            nombre = input("Ingresa Pelicula (cualquier valor): ")
            while nombre.isnumeric() or nombre.count(" ")>=3 or len(nombre)<=4:
                nombre = input("Ingresa Pelicula: ")
                
            genero = input("Ingresa genero de la pelicula (accion,fantasia,ficcion): ")
            while not genero.strip().lower() in ["accion","fantasia","ficcion"]:
                genero =input("Ingresa el genero de la pelicula: ")
                
            fecha = int(input("Ingresa fecha de emision(2008-2020): "))
            while not 2008<=fecha<=2020:
                fecha=int(input("Ingresa fecha de emision: "))
                
            estudio = input("Ingresa el estudio(Marvel): ")
            while not estudio.strip().lower() == "marvel":
                estudio=input("Ingresa el estudio: ")

            fase = int(input("Ingresa la fase de la pelicula(1-3): "))
            while not 1<=fase<=3:
                fase = int(input("Ingresa la fase de la pelicula: "))
            return nombre.capitalize(),genero.capitalize(),fecha,estudio.capitalize(),fase
        except ValueError:
            continue
def validacion1():
    while True:
        director = input("Ingresa el nombre del director: ")
        while director.isnumeric() or any(i.isnumeric() for i in director) or not director.isalpha() or len(director) <= 2 or director.count(" ") >= 2:
            director = input("Ingresa el nombre del director: ")
            
        genero = input("Ingresa el genero del director[F/M]: ")
        while not genero.lower() in ["f","m"]:
            genero = input("Ingresa el genero del director [F/M]: ")
        return director.capitalize(), genero.capitalize()
def validacion2():
    while True:
        nombre = input("Ingresa el nombre del actor: ")
        while nombre.isnumeric() or any(i.isnumeric() for i in nombre) or not nombre.isalpha() or len(nombre)<=4 or nombre.count(" ")>=2:
            nombre = input("Ingresa el nombre del actor: ")
        genero = input("Ingresa el genero del actor(f/m): ")
        while not genero.lower() in ["f","m"]:
            genero = input("Ingresa el genero del actor: ")
        nacionalidad = input("Ingrese la nacionalidad: ")
        while nacionalidad.isnumeric() or any(i.isnumeric() for i in nacionalidad) or not nacionalidad.isalpha() or len(nacionalidad)<=3 or nacionalidad.count(" ")>=4:
            nacionalidad = input("Ingrese la nacionalidad: ")
        interprete = input("Ingresa personaje a interpretar: ")
        while interprete.isnumeric() or any(i.isnumeric() for i in interprete) or not interprete.isalpha() or len(interprete)<=2 or nombre.count(" ")>=4:
            interprete = input("Ingresa personaje a interpretar: ")
        return nombre.capitalize(), genero.capitalize(),nacionalidad.capitalize(),interprete.capitalize()

    
def validacion3():
    while True:
        genero = input("Ingrese genero del personaje(f/m): ")
        while not genero.lower() in ["f","m"]:
            genero = input("Ingrese genero del personaje(f/m): ")
        return genero.capitalize()
    
    
#DECLARACION DE CLASES





    
        
class Pelicula:
    NombrePelicula= ""
    GeneroPelicula=""
    FechaEmision = 0
    Estudio=""
    Fase=0
    def __init__(self):
        Pelicula.NombrePelicula, Pelicula.GeneroPelicula, Pelicula.FechaEmision, Pelicula.Estudio, Pelicula.Fase = validacion()
        Pelicula.Estudio = ["accion","fantasia","ficcion"]
    def imprimir(self):
        print(Pelicula.NombrePelicula)
        print(Pelicula.GeneroPelicula)
        print(Pelicula.FechaEmision)
        print(Pelicula.Estudio)
        print(Pelicula.Fase)
        
class Director:
    def __init__(self):
        self.director, self.genero=validacion1()
    def imprimir(self):
        print(f"Nombre Director: {self.director}")
        print(f"Genero Director: {self.genero}")
        
directores=[]
registro = 0
while True:
    registro+=1
    print(f"-Registro Nro {registro}")
    directorx = Director()
    directores.append(directorx)
    print("DATOS INGRESADOS")
    directorx.imprimir()
    print()
    print("TOTAL DIRECTORES")
    for i in range(len(directores)):
        print(f"-Registro nro {i+1}:")
        directores[i].imprimir()
    print()
    opcion = input("Quieres ingresar otro director? (si/no): ").lower().strip()
    if opcion in ["no","n"]:
        break

class Actor:
    def __init__(self):
        self.nombre, self.genero,self.nacionalidad,self.interprete = validacion2()
    class Personaje(self):
        def _init__(self):
            self.personaje=self.interprete
            self.genero = validacion3()
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Genero: {self.genero}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Interprete: {self.interprete}")
actores = []
registro1= 0
while True:
    registro1+=1
    print(f"Registro nro{registro1}")
    actorx = Actor()
    actores.append(actorx)
    print("DATOS INGRESADOS")
    actorx.imprimir()
    print()
    print("TOTAL ACTORES")
    for i in range(len(actores)):
        print(f"-Registro {i+1}")
        actores[i].imprimir()
    print()
    opcion1=input("Quieres ingresar otro actor? (si/no): ").lower().strip()
    if opcion1 in ["no","n"]:
        break
        
