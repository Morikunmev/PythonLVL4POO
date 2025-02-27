class Persona:
    def inicializar(self,nombre,edad):
        self.nombre = nombre
        self.edad
    def imprimir(self):
        print("nombre: ",self.nombre)
        print("edad: ",self.edad)
    def MayorEdad(self):
        if self.edad >=18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
persona1 = Persona()
persona1.inicializar("Luis",23)
persona1.imprimir()
