class Socio:

    def __init__(self):
        self.nombre = input("Ingrese nombre de socio: ")
        self.antiguedad = int(input("Ingrese la antiguedad: "))
    def imprimir(self):
        print(self.nombre,"tiene una antiguedad de",self.antiguedad)
    def retornar_antiguedad(self):
        return self.antiguedad
class Club:
    def __init__(self):
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()
    def mayor_antiguedad(self):
        print("Socio con mayor antiguedad")
        if self.socio1.retornar_antiguedad()>self.socio2.retornar_antiguedad() and self.socio1.retornar_antiguedad()>self.socio3.retornar_antiguedad():
            self.socio1.imprimir()
        elif self.socio2.retornar_antiguedad()>self.socio1.retornar_antiguedad() and self.socio2.retornar_antiguedad()>self.socio3.retornar_antiguedad():
            self.socio2.imprimir()
        else:
            self.socio3.imprimir()
club1 = Club()
club1.mayor_antiguedad()