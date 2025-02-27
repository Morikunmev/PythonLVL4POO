class Alumno:
    def __init__(self):
        self.nombres = []
        self.notas = []
    def menu(self):
        opcion = 0
        while opcion!=4:
            print("1 - Carga de alumnos")
            print("2 - Listado de alumnos")
            print("3 - Listado de alumnos con notas mayores o iguales a 7")
            print("4 Finalizar el programa")
            opcion = int(input("Ingrese su opcion: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.nota_superior()
    def cargar(self):
        for x in range(5):
            nombre = input("Ingrese el nombre del alumno: ")
            nota = int(input("Ingrese la nota: "))
            self.nombres.append(nombre)
            self.notas.append(nota)
    def listar(self):
        for x,valor in enumerate(self.nombres):
            print(f"registro nro: {x+1}: nombre: {valor},nota: {self.notas[x]}")
    def nota_superior(self):
        print("Notas iguales o superiores a 7")
        for x, valor in enumerate(self.notas):
            if valor >=7:
                print(f"registro nro {x+1}, nombre: {self.nombres[x]}, nota: {valor}")

alumnos1 = Alumno()
alumnos1.menu()


