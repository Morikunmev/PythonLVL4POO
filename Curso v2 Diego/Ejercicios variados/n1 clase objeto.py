class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("nota: ",self.nota)

    def estado(self):
        if self.nota >=4:
            print(self.nombre,"esta regular")
        else:
            print(self.nombre,"esta libre")
alumno1 = Alumno()
alumno1.inicializar("juan",2)
alumno1.imprimir()
alumno1.estado()

alumno2 = Alumno()
alumno2.inicializar("ana",10)
alumno2.imprimir()
alumno2.estado()
