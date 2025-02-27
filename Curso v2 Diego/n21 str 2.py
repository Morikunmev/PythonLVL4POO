class Familia:
    def __init__(self,padre,madre,hijos = ["No tiene hijos"]):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
    def __str__(self):
        cadena = f"Nombre del padre: {self.padre}, Nombre de la madre: {self.madre}, Nombre de los hijos: "
        if self.hijos != ["No tiene hijos"]:
            cadena+=", ".join(self.hijos)
            return cadena
        else:
            cadena+=", ".join(self.hijos)
            return cadena
familia1 = Familia("Pablo","Ana",["Carlos","Veronica"])
familia2 = Familia("Jorge","Carla")
familia3 = Familia("Luis","Maria",["Marcos"])

print(familia1)
print(familia2)
print(familia3)