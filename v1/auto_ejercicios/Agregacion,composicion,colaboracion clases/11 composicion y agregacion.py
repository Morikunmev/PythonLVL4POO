class Bodega:
    def __init__(self,IdBodega = None,CapacidadBodega =None ,DireccionBodega = None,JefedeCargo = None):
        self.idbodega = IdBodega
        self.capacidad = CapacidadBodega
        self.direcccion = DireccionBodega
        self.jefe = JefedeCargo
    def ListarProductos(self,a):
        for i in range(len(a)):
            print(f"Producto nro {i+1}: {a[i]}")
    def ContarProducto(self,a):
        print(f"{a} elementos registrados")
    def PrecioXCantidad(self,a,b):
        ListaPrecioXCantidad = []
        for i in range(len(a)):
            precioxcantidad = a[i] * b[i]
            ListaPrecioXCantidad.append(precioxcantidad)
        print(ListaPrecioXCantidad)
    def PrecioXStockl(self,a,b):
        listapreciostock = []
        for i in range(len(a)):
            preciostock = a[i] * b[i]
            listapreciostock.append(preciostock)
        print(listapreciostock)
class Empleado:
    ListaUsuario = []
    ListaContraseña = []

    def __init__(self,Rut = None,NombreCompleto = None,DiaNacimiento = None,MesNacimiento = None, AñoNacimiento = None):
        self.rut = Rut
        self.nombre = NombreCompleto
        self.dia_nacimiento = DiaNacimiento
        self.mes_nacimiento = MesNacimiento
        self.año_nacimiento = AñoNacimiento
    def AgregarUsuario(self,Usuario):
        Empleado.ListaUsuario.append(Usuario)
    def AgregarContraseña(self,Contraseña):
        Empleado.ListaContraseña.append(Contraseña)

class Producto:
    contador = 0
    ListaNombre = []
    ListaPrecio = []
    ListaCantidad = []
    ListaStock = []

    def __init__(self,CodigoBarra = None,NombreProducto = None,CategoriaProducto = None,Marca = None,Precio = None,Cantidad = None,Stock = None):
        self.codigo = CodigoBarra
        self.nombre = NombreProducto
        self.categoria = CategoriaProducto
        self.marca = Marca
        self.precio = Precio
        self.cantidad = Cantidad
        self.stock = Stock
        Producto.contador+=1

        Producto.ListaPrecio.append(self.precio)
        Producto.ListaCantidad.append(self.cantidad)
        Producto.ListaNombre.append(self.nombre)
        Producto.ListaStock.append(self.stock)

bod1 =Bodega(1,200,"Santa Maria","Karlos")

empleado1 = Empleado("19.662.924-6","Richard",30,12,1998)
empleado2 = Empleado("20.333.333-6","hola",12,3,2000)
empleado3 = Empleado ("20.300.400-1","hofo",20,3,2001)

empleado1.AgregarUsuario("Richard")
empleado1.AgregarContraseña(222)
empleado2.AgregarUsuario("Nicolas")
empleado2.AgregarContraseña(22222)
empleado3.AgregarUsuario("Felipe")
empleado3.AgregarContraseña(111)


producto1 = Producto(1,"Leche","Bebida","Nestle",1200,100,5)
producto2 = Producto(2,"Coca Cola","Agua","Nose",500,120,1)
producto3 = Producto(3,"Carne","Xd","Nwqewq",12,112,45)
producto4 = Producto(4,"Yogurt","Agua","hfhf",150,14,4)


while True:
    usuario = input("Ingrese su usuario: ")
    contraseña = int(input("Ingrese su contraseña: "))
    for i in range(len(Empleado.ListaUsuario)):
        if usuario == Empleado.ListaUsuario[i] and contraseña == Empleado.ListaContraseña[i]:
            opcion = int(input("Ingrese su opcion: "))
            if opcion == 1:
                bod1.PrecioXCantidad(Producto.ListaCantidad, Producto.ListaPrecio)
            elif opcion == 2:
                bod1.PrecioXStockl(Producto.ListaPrecio, Producto.ListaStock)
            elif opcion == 3:
                bod1.ListarProductos(Producto.ListaNombre)
