def enterodef():
    while True:
        try:
            valor = int(input("Ingresa un valor: "))
            if valor <=0:
                continue
            return valor
        except ValueError:
            continue
        
class Operaciones:
    def __init__(self):
        suma=0
        for i in range(4):
            print(f"Valor nro {i+1}")
            valor= enterodef()
            suma+=valor
        self.suma=suma
    def promedio(self):
        prod=self.suma/4
        print(f"El promedio es: {prod}")
operacion1 = Operaciones()
operacion1.promedio()
