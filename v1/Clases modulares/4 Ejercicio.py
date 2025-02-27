from Validacion import generaldef
class Numero:
    def __init__(self):
        self.num1=generaldef.entero1def("Ingresa numero 1: ")
        self.num2=generaldef.entero1def("Ingresa numero 2: ")
        self.num3=generaldef.entero1def("Ingresa numero 3: ")
        self.num4=generaldef.entero1def("Ingresa numero 4: ")
    def imprimir(self):
        print("Valores ingresados: " + str(self.num1) + ", " +str(self.num2) + ", " +str(self.num3) + ", " + str(self.num4))
    def calculo(self):
        self.suma=self.num1 + self.num2
        self.producto=self.num3 * self.num4
        print("La suma es:" ,self.suma)
        print("El producto es: ",self.producto)

numero1 = Numero()
numero1.imprimir()
numero1.calculo()
