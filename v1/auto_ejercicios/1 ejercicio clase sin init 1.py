def clase_1():
    class Persona:

        def inicializar(self, nom1,nom2):
            self.nombre=[nom1,nom2]
        def imprimir(self):
            print("Nombre",self.nombre)
    #bloque principal
    persona1=Persona()
    #llamar al metodo inicializar
    persona1.inicializar("Pedro","Alberto")
    persona1.imprimir()

    persona2=Persona()
    persona2.inicializar("Ana","Persona")
    persona2.imprimir()

clase_1()
