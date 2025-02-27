class Rectangulo:
    def __init__(self,ladomenor,ladomayor):
        self.ladomenor = ladomenor
        self.ladomayor = ladomayor
    def retornar_superficie(self):
        return self.ladomenor * self.ladomayor
    def __eq__(self, other):
        if self.retornar_superficie() == other.retornar_superficie():
            return True
        else:
            return False
    def __ne__(self, other):
        if self.retornar_superficie() != other.retornar_superficie():
            return True
        else:
            return False
    def __gt__(self, other):
        if self.retornar_superficie() > other.retornar_superficie():
            return True
        else:
            return False
    def __ge__(self, other):
        if self.retornar_superficie() >= other.retornar_superficie():
            return True
        else:
            return False
    def __lt__(self, other):
        if self.retornar_superficie() < other.retornar_superficie():
            return True
        else:
            return False
    def __le__(self, other):
        if self.retornar_superficie() <= other.retornar_superficie():
            return True
        else:
            return False

rectangulo1 = Rectangulo(11,10)
rectangulo2 = Rectangulo(5,20)

def funcion6():
    if rectangulo1 < rectangulo2:
        print("rectangulo 1 es menor o igual que rectangulo 2")
def funcion5():
    if rectangulo1 < rectangulo2:
        print("rectangulo 1 es menor que rectangulo 2")
def funcion4():
    if rectangulo1 >= rectangulo2:
        print("rectangulo 1 es mayor o igual que rectangulo 2")
def funcion1():
    if rectangulo1 == rectangulo2:
        print("Los rectangulos tienen la misma superficie")
def funcion2():
    if rectangulo1 != rectangulo2:
        print("No tienen la misma superficie")
def funcion3():
    if rectangulo1 > rectangulo2:
        print("rectangulo 1 es mayor que rectangulo 2")

funcion4()
