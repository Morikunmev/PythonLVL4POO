class Juego:
    nombre = ""
    edad = 0
    def inicio(self):
        Juego.nombre = "Richard"
        Juego.edad = 24
        
    def imprimir(self):
        print("Nombre: ",Juego.nombre)
        print("Edad: ", Juego.edad)

juego1=Juego()
juego1.inicio()
juego1.imprimir()
print()
juego2=Juego()
juego2.inicio()
juego2.imprimir()
