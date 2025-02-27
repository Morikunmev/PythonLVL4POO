class Bodega:
    def __init__(self,IdBodega = None,CapacidadBodega =None ,DireccionBodega = None,JefedeCargo = None):
        self.idbodega = IdBodega
        self.capacidad = CapacidadBodega
        self.direcccion = DireccionBodega
        self.jefe = JefedeCargo
    def ContarProducto(self,a):
        print(f"{a} productos registrados")
    def PrecioxCantidad(self,a,b):
        ListaxCantidad = []
        for i in range(len(a)):
            PrecioxCantidad = a[i] * b[i]
            ListaxCantidad.append(PrecioxCantidad)
        print(ListaxCantidad)
    def PrecioxStock(self,a,b,c):
        ListaPrecioxStock = []
        for i in range(len(a)):
            PrecioxStock = a[i] * b[i]
            ListaPrecioxStock.append(PrecioxStock)
        for x in range(len(a)):
            print(f"Elemento nro {x+1}, {c[x]}, {ListaPrecioxStock[x]}")
class Empleado:
    ListaUsuario = ["Richard","Marcos","Alejandra"]
    ListaContraseña = [1234,12345,123456]

    def __init__(self,Rut = None,NombreCompleto = None,DiaNacimiento = None,MesNacimiento = None, AñoNacimiento = None):
        self.rut = Rut
        self.nombre = NombreCompleto
        self.dia_nacimiento = DiaNacimiento
        self.mes_nacimiento = MesNacimiento
        self.año_nacimiento = AñoNacimiento
class Producto:
    contador = 0
    nombre = []
    precio = []
    cantidad = []
    stock = []

    def __init__(self,CodigoBarra = None,NombreProducto = None,CategoriaProducto = None,Marca = None,Precio = None,Cantidad = None,Stock = None):
        self.codigo = CodigoBarra
        self.nombre = NombreProducto
        self.categoria = CategoriaProducto
        self.marca = Marca
        self.precio = Precio
        self.cantidad = Cantidad
        self.stock = Stock
        Producto.contador+=1

        Producto.precio.append(self.precio)
        Producto.cantidad.append(self.cantidad)
        Producto.nombre.append(self.nombre)
        Producto.stock.append(self.stock)


bod1 =Bodega(1,200,"Santa Maria","Karlos")

empleado1 = Empleado("19.662.924-6","Richard",30,12,1998)
empleado2 = Empleado("20.333.333-6","hola",12,3,2000)
empleado3 = Empleado ("20.300.400-1","hofo",20,3,2001)

producto1 = Producto(1,"Leche","Bebida","Nestle",1200,100,5)
producto2 = Producto(2,"Coca Cola","Agua","Nose",500,120,1)
producto3 = Producto(3,"Carne","Xd","Nwqewq",12,112,45)
producto4 = Producto(4,"Yogurt","Agua","hfhf",150,14,4)


while True:
    usuario = input("Ingrese usuario: ")
    contraseña = int(input("Ingrese contraseña: "))
    for i in range(len(Empleado.ListaUsuario)):
        if usuario == Empleado.ListaUsuario[i] and contraseña == Empleado.ListaContraseña[i]:
            opcion = int(input("que quiere hacer?: "))
            if opcion == 1:
                bod1.ContarProducto(Producto.contador)
            elif opcion == 2:
                bod1.PrecioxCantidad(Producto.cantidad, Producto.precio)
            elif opcion == 3:
                bod1.PrecioxStock(Producto.precio, Producto.stock, Producto.nombre)
