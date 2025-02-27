#Entreada de usuario dentro de la clase
def forma1():
    class Numero:
        def __init__(self):
            self.numero1=int(input("Ingresa un numero: "))
            self.numero2=int(input("Ingresa otro numero: "))
        def imprimir(self):
            print(self.numero1)
            print(self.numero2)
        def calculo(self):
            self.producto=self.numero1 * self.numero2
            self.suma=self.numero1 + self.numero2
            print("La multiplicacion es: ",self.producto)
            print("La suma es:",self.suma)
    numero1=Numero()
    numero1.imprimir()
    numero1.calculo()
#Asignacion de variable en el bloque principal
def forma2():
    class Numero:
        def __init__(self,n1,n2):
            self.n1=n1
            self.n2=n2
        def imprimir(self):
            print("Numero 1",self.n1)
            print("Numero 2",self.n2)
        def calculo(self):
            self.producto=self.n1 * self.n2
            self.suma= self.n1 + self.n2
        def imprimir_producto(self):
            print("Podructo de los 2 numeros: ", self.producto)
            print("Suma de los 2 numeros: ",self.suma)
    numero1=Numero(2,3)
    numero1.imprimir()
    numero1.calculo()
    numero1.imprimir_producto()

#Asignacion de variable en el bloque principal, la clase esta en forma modular
def forma3():
    class Numero:
        def __init__(self,n1,n2):
            self.n1=n1
            self.n2=n2
        def productodef(self):
            return self.n1*self.n2
        def sumadef(self):
            return self.n1+self.n2
        def calculo(self):
            self.producto=self.productodef()
            self.suma=self.sumadef()
            print("El producto es: ",self.producto)
            print("La suma es:",self.suma)
    numero1 = Numero(2,3)
    numero1.calculo()
forma3()
