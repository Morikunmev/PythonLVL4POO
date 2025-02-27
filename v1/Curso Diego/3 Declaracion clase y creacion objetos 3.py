#Cofeccionar una clase que permita cargar el nombre y la edad de una persona.
#Mostrar los datos cargados
#Imprimir un mensaje si es mayor de edad (edad>=18)

class Persona:
    def datos(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def imprimir(self):
        print(self.nombre)
        print(self.edad)
    def mayor(self):
        if self.edad >=18:
            print("Es mayor")
        else:
            print("Es menor")

persona1 = Persona()
persona1.datos("Richard",24)
persona1.imprimir()
persona1.mayor()
