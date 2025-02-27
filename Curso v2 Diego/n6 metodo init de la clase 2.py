class Punto:
    def __init__(self,x=None,y=None):
        self.x = x
        self.y = y
    def imprimir(self):
        print("Coordenada del punto: ")
        print(f"({self.x},{self.y})")
    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("primer cuadrante")
        elif self.x<0 and self.y>0:
            print("segundo cuadrante")
        elif self.x<0 and self.y<0:
            print("tercer cuadrante")
        elif self.x>0 and self.y<0:
            print("cuarto cuadrante")
        else:
            print("esta en un eje")

punto1 = Punto()
punto1.imprimir()
punto1.imprimir_cuadrante()