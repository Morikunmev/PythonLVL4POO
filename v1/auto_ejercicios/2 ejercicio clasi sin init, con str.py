class Persona:
    def inicializar(self, nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)
    def __str__(self):
        return f"Persona(nombre={self.nombre})"

persona1 = Persona()
persona1.inicializar("Pedro")
persona1.imprimir()
persona1.__str__()


