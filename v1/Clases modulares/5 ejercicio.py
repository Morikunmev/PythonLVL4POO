from Validacion import generaldef
class Numero:
    def __init__(self):
        self.n1 =generaldef.entero1def("Ingrese un numero (1): ")
        self.n2 =generaldef.entero1def("Ingrese un numero (2): ")
        self.n3 =generaldef.entero1def("Ingrese un numero (3): ")
        self.n4 =generaldef.entero1def("Ingrese un numero (4): ")
    def imprimir(self):
        print("Valores ingreados: ")
        print("Valor 1: ",self.n1)
        print("Valor 2: ",self.n2)
        print("Valor 3: ",self.n3)
        print("Valor 4: ",self.n4)
    def calculo(self):
        self.suma=self.n1 + self.n2 + self.n3 + self.n4
        self.promedio=self.suma/4
        print("La suma de los 4 numeros es: ",self.suma)
        print("El promedio de los 4 numeros es: ",self.promedio)

numero1 = Numero()
numero1.imprimir()
numero1.calculo()
