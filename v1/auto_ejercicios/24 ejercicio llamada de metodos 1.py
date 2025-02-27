class Alumno:
    def __init__(self):
        self.nombres = []
        self.notas = []
    def menu(self):
        opcion = 0
        while opcion!= 5:
            print("1. Cargar Alumnos y Notas")
            print("2. Listado Alumnos Notas")
            print("3. Listado Alumnos con notas mayores o iguales a 7")
            print("4. Eliminar Nota")
            print("5. Finalizar el programa")
            opcion = int(input("Elige una opcion: "))
            if opcion ==1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion ==3:
                self.mayor()
            elif opcion ==4:
                self.eliminar()


    def listar(self):
        for i in range(len(self.nombres)):
            print(f"Registro nro {i+1}: {self.nombres[i]}, Notas: {self.notas}")
    def cargar(self):
        self.nombres.append(input("Ingrese el nombre"))
        self.notas.append(int(input("Ingresa la nota")))
    def mayor(self):
        for i in range(len(self.notas)):
            if self.notas[i]>=7:
                print(self.nombres[i],self.notas[i])
    def eliminar(self):
        eliminar = input("Ingrese el registro a eliminar: ")
        if eliminar in self.nombres:
            index = self.nombres.index(eliminar)
            del self.nombres[index]
            del self.notas[index]
            print(F"Se ha eliminado a: ",eliminar)
        else:
            print("No se ha podido encontrar")

alumno1 = Alumno()
alumno1.menu()