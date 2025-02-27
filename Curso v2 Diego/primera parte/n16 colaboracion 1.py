class Cliente:
    def __init__(self,nombre,monto):
        self.nombre = nombre
        self.monto = monto
    def sumar(self,objeto):
        suma = self.monto + objeto
        print(f"La suma es: {suma}")
    def suma1(self,objeto):
        suma = self.monto + objeto
        return suma
    def __add__(self, a):
        suma = self.monto + a.monto
        return suma

cliente1 = Cliente("Richard",1222)
cliente2 = Cliente("Skarlett",2009)
print(cliente1 + cliente2)
