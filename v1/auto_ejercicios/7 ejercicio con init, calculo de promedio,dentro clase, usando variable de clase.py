class Alumno:
    suma=0
    def __init__(self):
        for i in range(4):
            print(f"Valor nro{i+1}")
            valor=int(input("Ingresa: "))
            Alumno.suma+=valor
    def promedio(self):
        prod=Alumno.suma/4
        print(f"El promedio es: {prod}")
alumno1=Alumno()
alumno1.promedio()

alumno2=Alumno()
alumno2.promedio()
