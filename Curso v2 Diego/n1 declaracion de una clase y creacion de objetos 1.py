class Persona:
    def inicializar(self,nombre):
        self.nombre = nombre
    def Imprimir(self):
        print(f"Nombre: {self.nombre}")

persona1 = Persona()
persona1.inicializar("Richard")
persona1.Imprimir()

persona2 = Persona()
persona2.inicializar("Ana")
persona2.Imprimir()