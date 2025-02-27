class Personaje:
    ListaGeneral = []
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Genero: ",self.genero)
        self.estado()

    def estado(self):
        if self.nombre in Personaje.ListaGeneral:
            print("ACTIVO")
        else:
            print("DESACTIVO")
    def añadir(self):
        Personaje.ListaGeneral.append(self.nombre)

personaje1 = Personaje("Richard","F")
personaje1.añadir()

personaje1.imprimir()
