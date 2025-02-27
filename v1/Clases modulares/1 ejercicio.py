from Validacion import generaldef,operaciones_simples as simple

class Numero:
    def __init__(self):
        self.numero1=generaldef.enterodef("Ingresa un numero: ")
        self.numero2=generaldef.enterodef("Ingresa otro numero: ")
    def imprimir(self):
        print("La suma es:",simple.suma(self.numero1,self.numero2))
        print("la resta es:",simple.resta(self.numero1,self.numero2))
        print("La multiplicacion es:",simple.multiplicacion(self.numero1,self.numero2))
        print("La division es:",simple.division(self.numero1,self.numero2))


numero1=Numero()
numero1.imprimir()
        
