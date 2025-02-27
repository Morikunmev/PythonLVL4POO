def enterodef():
    while True:
        try:
            x = int(input("Ingresa valor de x: "))
            y = int(input("Ingresa valor de y: "))
            return x,y
        except ValueError:
            continue

class Plano:
    def __init__(self):
        self.x,self.y = enterodef()
    def cuadrante(self):
        if self.x >0 and self.y>0:
            print("Se encuentra en el primer cuadrante")
        elif self.x<0 and self.y>0:
            print("Se encuentra en el segundo cuadrante")
        elif self.x<0 and self.y<0:
            print("Se encuentra en el tercer cuadrante")
        else:
            print("Se encuentra en el cuarto cuadrante")

plano1 = Plano()
plano1.cuadrante()
