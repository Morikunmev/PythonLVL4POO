class Persona:
    def inicializar(self,nombre,edad):
        self.nombre = nombre.capitalize()
        self.edad = edad
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
    def estado(self):
        if self.edad >=18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

persona1 = Persona()
persona1.inicializar("richard",24)
persona1.imprimir()

persona2 = Persona()
persona2.inicializar("felipe",21)
persona2.imprimir()