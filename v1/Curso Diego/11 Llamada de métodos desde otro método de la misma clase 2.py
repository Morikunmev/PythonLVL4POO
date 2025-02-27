class Alumnos:
    def __init__(self):
        self.nombre = []
        self.notas = []
    def menu(self):
        opcion = 0
        while opcion != 4:
            print("1.Cargar Alumnos")
            print("2.Listado de Alumnos")
            print("3.Listado de Alumnos con notas mayores o iguales a 7")
            print("4.Finalizar el programa")
            opcion = int(input("Ingrese su opcion: "))
            if opcion ==1:
                self.cargar()
            elif opcion ==2:
                self.listar()
            elif opcion ==3:
                self.NotasAltas
    def cargar(self):
        for i in range(5):
            nom=input(f"Ingrese el nombre del alumno {i+1}: ")
            self.nombre.append(nom)
            no=int(input(f"Ingrese la nota de {nom}: "))
            self.notas.append(no)
    def listar(self):
        print("Listado Completo de Alumnos")
        for i in range(5):
            print(self.nombre[i],self.notas[i])
    def NotasAltas(self):
        print("Listado de Notas altas")
        for i in range(5):
            if self.notas[i]>=7:
                print(self.nombre[i], self.notas[i])

alumno = Alumnos()
alumno.menu()