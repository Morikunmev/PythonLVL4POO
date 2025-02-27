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


class Actor:
    def __init__(self):
        self.nombre, self.genero,self.nacionalidad,self.interprete = validacion2()
        self.personaje = self.Personaje(self.interprete)
    class Personaje:
        def __init__(self,interprete):
            self.personaje= interprete
        def imprimir(self):
            self.genero=validacion3()
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Genero: {self.genero}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Interprete: {self.interprete}")

actor1 = Actor()
actor1.imprimir()
personaje = actor1.Personaje
print(f"Personaje: {personaje.personaje}")
