class Galleta:
    chocolate = False
    def __init__(self):
        print("Se acaba de crear una galleta")
    def chocolatear(self):
        self.chocolate = True
    def tiene_chocolate(self):
        if self.chocolate:
            print("Soy una galleta con chocolate")
        else:
            print("Soy una galleta sin chocolate")

galleta1 = Galleta()
galleta1.chocolatear()
galleta1.tiene_chocolate()
galleta1.tamaño="Mediano"


