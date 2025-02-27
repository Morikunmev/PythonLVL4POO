class Cliente:
    NombresClientes = []
    CantidadClientes = 0
    def __init__(self,nombre = None):
        self.nombres = "nombre desconocido" if nombre is None else nombre.capitalize()

        Cliente.CantidadClientes+=1
        Cliente.NombresClientes.append(self.nombres)
        Producto.nombres.clear()
        Producto.precios.clear()
    def imprimir(self):
        print("Nombre cliente: ",self.nombres)
        print("Cantidad de clientes: ",Cliente.CantidadClientes)
    def agregar_producto(self,nombre,precio):
        self.producto = Producto(nombre,precio)
    def imprimir_compras(self):
        print(f"todas las compras de: {self.nombres}")
        self.producto.imprimir_agregados()
class Producto:
    nombres = []
    precios = []
    def __init__(self,nombre = None,precio = None):
        self.nombre = nombre
        self.precio = precio

        self.cantidad = 0
        self.cantidad+=1

        Producto.nombres.append(self.nombre)
        Producto.precios.append(self.precio)

        Supermercado.RegistroNombreProducto.append(self.nombre)
        Supermercado.RegistroPrecioProducto.append(self.precio)
    def imprimir_agregados(self):
        for i, (productos, precios) in enumerate(zip(Producto.nombres,Producto.precios)):
            print(f"Registro nro {i+1}: producto: {productos}, precio: {precios}")
class Supermercado:
    RegistroNombreProducto = []
    RegistroPrecioProducto = []
    def __init__(self,nombre):
        self.nombre = nombre
    def imprimir_total(self):
        print(f"Todos los productos del supermercado {self.nombre} ")
        for i, (producto,precio) in enumerate(zip(Supermercado.RegistroNombreProducto,Supermercado.RegistroPrecioProducto)):
            print(f"Registro nro {i+1}, producto: {producto}, precio: {precio}")
    def calcular_suma(self):
        print("Suma total de precios de los clientes")
        suma = sum(Supermercado.RegistroPrecioProducto)
        print(suma)

supermercado1 = Supermercado("HELADERIA")

cliente1 = Cliente("richard")
cliente1.imprimir()
cliente1.agregar_producto("leche",1000)
cliente1.agregar_producto("chocolate",2000)
cliente1.agregar_producto("energy",1950)
cliente1.agregar_producto("coca cola",3000)
cliente1.imprimir_compras()

print()
cliente2 = Cliente("juan")
cliente2.imprimir()
cliente2.agregar_producto("moster",1000)
cliente2.imprimir_compras()

print()
supermercado1.imprimir_total()
supermercado1.calcular_suma()