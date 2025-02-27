class Lista:
    def __init__(self,lista):
        self.lista = lista
    def imprimir(self):
        print(self.lista)
    def __add__(self, other):
        nueva = []
        for i, valor in enumerate(self.lista):
            nueva.append(valor + other)
        return nueva
    def __sub__(self, other):
        nueva = []
        for i, valor in enumerate(self.lista):
            nueva.append(valor - other)
        return nueva
    def __mul__(self, other):
        nueva = []
        for i, valor in enumerate(self.lista):
            nueva.append(valor * other)
        return nueva
    def __floordiv__(self, other):
        nueva = []
        for i, valor in enumerate(self.lista):
            nueva.append(valor // other)
        return nueva
lista1 = Lista([2,2,2,2,2])
lista1.imprimir()
print(lista1 // 2)