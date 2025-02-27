class Agenda:
    def __init__(self):
        self.contactos={}
    def menu(self):
        opcion = 0
        while opcion!=5:
            print("1 - Carga de un contacto en la agenda")
            print("2 - Listado completo de la agenda")
            print("3 - Consulta ingresando el nombre de una persona")
            print("4 - Modificacion del telefono y mail")
            print("5 - Finalizar el programa")
            opcion = int(input("Ingrese su opcion"))
            if opcion ==1:
                self.cargar()
            elif opcion ==2:
                self.listado()
            elif opcion ==3:
                self.consulta()
            elif opcion ==4:
                self.modificacion()
    def cargar(self):
        nombre = input("Ingrese el nombre de la persona: ")
        telefono = input("Ingrese el telefono: ")
        mail = input("Ingrese el mail: ")
        self.contactos[nombre]= (telefono,mail)
    def listado(self):
        print("Listado de la agenda")
        for i in self.contactos:
            print(i, self.contactos[i][0],self.contactos[i][1])
    def consulta(self):
        nombre = input("Ingrese el nombre de la persona a consultar: ")
        if nombre in self.contactos:
            print(nombre,"su telefono es: ",self.contactos[nombre][0], "y su mail es: ",self.contactos[nombre][1])
        else:
            print("No exite un contacto con dicho nombre")
    def modificacion(self):
        nombre = input("Ingrese el nombre de la persona a modificar su telefono y mail")
        if nombre in self.contactos:
            telefono=input("Ingrese nuevo telefono")
            mail = input("Ingrese el nuevo mail")
            self.contactos[nombre]=(telefono,mail)
        else:
            print("No existe un contacto con dicho nombre")
agenda1 = Agenda()
agenda1.menu()