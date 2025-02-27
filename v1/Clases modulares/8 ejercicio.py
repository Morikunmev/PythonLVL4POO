from Validacion import generaldef,operaciones_simples as simple

class Numero:
    def __init__(self):
        self.num1=generaldef.entero1def("Ingresa numero (1): ")
        self.num2=generaldef.entero1def("Ingresa numero (2): ")
    def imprimir(self):
        print(f"Numero 1: {self.num1}")
        print(f"Numero 2: {self.num2}")
    def condicional(self):
        mayor=simple.mayordef(self.num1,self.num2)
        print("El mayor es: ",mayor)
        menor=simple.menordef(self.num1,self.num2)
        print("El menor es: ",menor)

numero1 = Numero()
numero1.imprimir()
numero1.condicional()
