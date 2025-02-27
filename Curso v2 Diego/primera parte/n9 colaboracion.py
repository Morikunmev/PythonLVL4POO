#Tienda en linea

class Cliente:
    def __init__(self,nombre = None):
        self.nombre = "sin nombre" if nombre is None else nombre
        self.monto = 0
        self.cantidad = 0
    def agregar_compra(self, monto):
        self.monto+=monto
        self.cantidad+=1
        print("A pagar: ",self.monto)
        print("Cantidad de productos",self.cantidad)
    def devolver_compra(self,monto):
        self.monto-=monto
        self.cantidad-=1
        print("Devolder precio de: ",self.monto)
        print("Cantidad devuelta: ",self.cantidad)
    def retornar(self):
        return self.monto * self.cantidad
class Supermercado:
    def __init__(self,cliente = None):
        self.cliente = Cliente(cliente)
    def acciones_cliente(self):
        self.cliente.agregar_compra(1000)
        self.cliente.agregar_compra(2000)
        self.cliente.agregar_compra(3000)
        self.cliente.agregar_compra(2000)
    def imprimir_final(self):
        print(f"Precio total a pagar: ",self.cliente.retornar())
supermercado1 = Supermercado("Richard")
supermercado1.acciones_cliente()
supermercado1.imprimir_final()
