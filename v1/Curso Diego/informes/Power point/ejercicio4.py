class Galleta:
    chocolate = True

    def __init__(self,sabor="salada",forma="Mediana"):
        self.sabor = sabor
        self.forma = forma
        if sabor is not None and forma is not None:
            print(f"Se acaba de crear una galleta {self.sabor} y {self.forma}")

galleta1 = Galleta()

