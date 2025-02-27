class Empleador:

    def __init__(self):
        self.ListaNombre = []
        self.ListaSueldo = []
    def menu(self):
        opcion = 0
        while opcion!=4:
            print("1.CARGAR NOMBRE Y SUELDO: ")
            print("2.LISTAR NOMBRE Y SUELDO: ")
            print("3.ELIMINAR REGISTRO: ")
            print("4.SALIR DEL PROGRAMA: ")

            opcion = int(input("Seleccione una opcion: "))
            if opcion ==1:
                self.ListaNombre.append(input("Ingresa el nombre: "))
                self.ListaSueldo.append(int(input("Ingresa el sueldo: ")))
            elif opcion ==2:
                for i in range(len(self.ListaNombre)):
                    print(f"Registro nro {i+1}, Nombre: {self.ListaNombre[i]}, Sueldo: {self.ListaSueldo[i]}")
            elif opcion ==3:
                eliminar = input("Ingresa el nombre a eliminar: ")
                if eliminar in self.ListaNombre:
                    index = self.ListaNombre.index(eliminar)
                    del self.ListaNombre[index]
                    del self.ListaSueldo[index]
                    print("Se ha eliminado a: ",eliminar)
                else:
                    print("No se ha podido encontrar")

empleado1 = Empleador()
empleado1.menu()