class Agenda:
    def __init__(self):
        self.nombres = []
        self.telefono = []
        self.mail = []
    def menu(self):
        opcion = 0
        while opcion != 5:
            print("1. Carga de contacto en la agenda")
            print("2. Listado completo de la agenda")
            print("3. Consulta del nombre")
            print("4. Modificacion del telefono y el mail")
            print("5. Finalizar el programa")
            opcion = int(input("Eliga un opcion: "))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.consulta()
            elif opcion == 4:
                self.modificar()
    def cargar(self):
        nombre = input("Ingrese nombre: ")
        telefono = int(input("Ingrese telefono: "))
        mail = input("Ingrese mail: ")
        self.nombres.append(nombre)
        self.telefono.append(telefono)
        self.mail.append(mail)
    def listar(self):
        for indice, (nombre, telefono, mail) in enumerate(zip(self.nombres, self.telefono, self.mail)):
            print(f"Registro nro {indice+1}: nombre: {nombre}, telefono: {telefono}, mail: {mail}")
    def consulta(self):
        con = input("Ingrese el nombre a consultar: ")
        if con in self.nombres:
            for (nombre,telefono,mail) in zip(self.nombres,self.telefono,self.mail):
                print(f"telefono de {nombre}: {telefono}, mail: {mail}")
    def modificar(self):
        mod = input("Ingrese el nombre a modificar: ")
        if mod in self.nombres:
            indice = self.nombres.index(mod)
            nombre = input(f"Ingrese el nuevo nombre de {mod}: ")
            telefono = int(input(f"Ingrese el nuevo telefono: "))
            mail = input("Ingrese el nuevo mail: ")

            self.nombres[indice] = nombre
            self.telefono[indice] = telefono
            self.mail[indice] = mail
        else:
            print("No se encuentra el registro")

agenda1 = Agenda()
agenda1.menu()














