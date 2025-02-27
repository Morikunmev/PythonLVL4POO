class Agenda:
    def __init__(self):
        self.contactos = {}
    def menu(self):
        opcion = 0
        while opcion!=5:
            print("1. Carga de un contacto en la agenda")
            print("2. Listado completo de la agenda")
            print("3. Consulta ingresando el nombre de una persona")
            print("4. Modificaciones del telefono y mail")
            print("5. Finalizar el programa")
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listado()
            elif opcion == 3:
                self.consulta()
            elif opcion == 4:
                self.modificacion()
    def cargar(self):
        nombre = input("Nombre: ")
        telefono = int(input("Telefono: "))
        mail = input("Mail: ")
        self.contactos[nombre]=(telefono,mail)
        print()
    def listado(self):
        for nombre, (telefono, mail) in self.contactos.items():
            print(f"nombre: {nombre}, telefono: {telefono}, mail: {mail}")
    def consulta(self):
        nombref = input("Ingrese el nombre de la persona a consultar: ")
        if nombref in self.contactos:
            print(f"Su telefono es: {self.contactos[nombref][0]}, y su mail es: {self.contactos[nombref][1]}")
    def modificacion(self):
        nombre = input("Ingrese el nombre de la persona a modificar: ")
        if (nombre in self.contactos):
            telefono = int(input("Ingrese nuevo contacto: "))
            mail = input("Ingrese nuevo mail: ")
            self.contactos[nombre]=(telefono,mail)
        else:
            print("No existe el nombre")
agenda1 = Agenda()
agenda1.menu()