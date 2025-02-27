class Circulo:
    def __init__(self,radio):
        self.__radio = radio
        self.__pi = 3.1415
    def calcularPerimetro(self):
        return 2 * self.__pi * self.__radio
    def calcularArea(self):
        return self.__pi * self.__radio**2
    def getPi(self):
        return self.__pi
    def setRadio(self,nuevo):
        if type(nuevo) == int or type(nuevo) == float:
            if nuevo>0:
                self.__radio = nuevo
                print(f"El radio se ha modificado correctamente: {self.__radio}")
            else:
                print("El radio no puede ser negativo")
        else:
            print("El radio tiene que ser un numero positivo")
c1 = Circulo(2.5)
print(c1.calcularArea())
print(c1.calcularPerimetro())
print(f"La constante PI es {c1.getPi()}")
c1.setRadio(34)
c1.setRadio("hola")
c1.setRadio(-1)

#atributo: __radio -> _circulo__radio . En general _NombreDeLaClase__nombreDelAtributo