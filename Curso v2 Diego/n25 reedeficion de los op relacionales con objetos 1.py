class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def __eq__(self, other):
        if self.edad == other.edad:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.edad != other.edad:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.edad > other.edad:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.edad >= other.edad:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.edad < other.edad:
            return True
        else:
            return False
    def __le__(self, other):
        if self.edad <= other.edad:
            return True
        else:
            return False

persona1 = Persona("Richard",24)
persona2 = Persona("Juan",22)
def funcion():
    if persona1 == persona2:
        print("Las dos personas tienen la misma edad")
    else:
        print("No tienen la misma edad")
def funcion1():
    if persona1 != persona2:
        print("Las dos personas no tienen la misma edad")
def funcion2():
    if persona1 > persona2:
        print("Richard es mayor que juan")
def funcion3():
    if persona1 >= persona2:
        print("Richard es mayor o igual que juan")
def funcion4():
    if persona1 < persona2:
        print("Richard es menor que juan")
    else:
        print("Juan es menor que Richard")
def funcion5():
    if persona1 <= persona2:
        print("Richard es menor o igual que juan")
    else:
        print("Juan es menor o igual que Richard")

funcion2()