class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def imprimir(self):
        print("Coordenada del punto")
        print(f"{self.x},{self.y}")
    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrante")
        elif self.x <0 and self.y>0:
            print("Segundo cuadrante")
        elif self.x<0 and self.y<0:
            print("Tercer cuadrante")
        elif self.x<0 and self.y<0:
            print("Cuarto cuadrante")
        else:
            print("Esta en un eje")

punto1=Punto(10,3)
punto1.imprimir()
punto1.imprimir_cuadrante()
print("-"*20)
punto2=Punto(0,0)
punto2.imprimir()
punto2.imprimir_cuadrante()
print("-"*20)
punto3=Punto(-1,-2)
punto3.__init__(0,0)
punto3.imprimir()
punto3.imprimir_cuadrante()
