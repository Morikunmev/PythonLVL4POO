class Galleta:
    chocolate = True

    def __init__(self,sabor,tamaño):
        self.sabor=sabor
        self.tamaño =tamaño
        print(f"Se acaba de crear una galleta {self.sabor} y {self.tamaño}")
    def chocolatear(self):
        self.chocolate=False
    def tiene_chocolate(self):
        if self.chocolate:
            print("Tiene chocolate")
        else:
            print("No tiene chocolate")
galleta1 = Galleta("Salada","Dulce")
