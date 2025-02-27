class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}),({self.y})"
punto1 = Punto(21,23)
punto2 = Punto(-21,3)
print(str(punto1))