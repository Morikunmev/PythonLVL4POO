#Declaracion por asignacion dentro de la clase
def forma1():
    class Cliente:
        def datos(self):
            self.nombre = "Richard"
            self.edad = 24
        def imprimir(self):
            print("Nombre:",self.nombre)
            print("Edad:",self.edad)

    cliente1 = Cliente()
    cliente1.datos()
    cliente1.imprimir()

#Declaracion entrada de datos dentro de la clase
def forma2():
    class Cliente:
        def datos(self):
            self.nombre = input("Ingresa nombre: ")
            self.edad = int(input("Ingresa edad: "))
        def imprimir(self):
            print("Nombre:",self.nombre)
            print("Edad:",self.edad)
    cliente1 = Cliente()
    cliente1.datos()
    cliente1.imprimir()
    
#Declaracion por entrada de datos dentro de la clase con validadcion
def forma3():

    def nombredef():
        while True:
            nombre = input("Ingrese nombre: ")
            if nombre.isnumeric() or any(i.isnumeric() for i in nombre) or not nombre.isalpha() or nombre.count(" ")>=1:
                continue
            return nombre.capitalize()
    def edaddef():
        while True:
            try:
                edad = int(input("Ingrese la edad: "))
                if edad <=0 or not 1<=edad<=100:
                    continue
                return edad
            except ValueError:
                continue
    class Cliente:
        def datos(self):
            self.nombre = nombredef()
            self.edad = edaddef()
        def imprimir(self):
            print("Nombre: ",self.nombre)
            print("Edad: ",self.edad)
    cliente1 = Cliente()
    cliente1.datos()
    cliente1.imprimir()

#Declaracion por entrada de datos dentro de la clase con validacion
def forma4():

    def nombredef():
        while True:
            nombre = input("Ingrese nombre: ")
            if nombre.isnumeric() or any (i.isnumeric() for i in nombre) or not nombre.isalpha() or nombre.count(" ")>=1:
                continue
            return nombre.capitalize()
    def edaddef():
        while True:
            try:
                edad = int(input("Ingrese edad: "))
                if edad <=0 or not 1<=edad<=150:
                    continue
                return edad
            except ValueError:
                continue
            
    class Cliente:
        def datos(self):
            self.nombre, self.edad =nombredef(),edaddef()
        def imprimir(self):
            print("Nombre:",self.nombre)
            print("Edad:",self.edad)
    cliente1 = Cliente()
    cliente1.datos()
    cliente1.imprimir()
forma4()
            
    
