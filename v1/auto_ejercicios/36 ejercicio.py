class Bodega:
    def __init__(self,IdBodega = None,CapacidadBodega =None ,DireccionBodega = None,JefedeCargo = None):
        self.idbodega = IdBodega
        self.capacidad = CapacidadBodega
        self.direcccion = DireccionBodega
        self.jefe = JefedeCargo
        self.elementos = []
        self.precio = []
        self.cantidad = []

    def MostrarElementosPrecioCantidad(self):
        print(f"Productos: {self.elementos}")
        print(f"Precios: {self.precio}")
        print(f"Cantidad: {self.cantidad}")
    def AgregarElementos(self,a):
        self.elementos.append(a)
    def AgregarPrecio(self,b):
        self.precio.append(b)
    def AgregarCantidad(self,c):
        self.cantidad.append(c)

    def ContarElementos(self):
        print(f"Total elementos agregados: {len(self.elementos)}")

    def CalcularCantidad(self):
        Cantidad = 0
        for i in range(len(self.cantidad)):
            Cantidad+= self.cantidad[i]

        print("La cantidad de producto es: ",Cantidad)
    def CalcularPrecio(self):
        Precio = 0
        for i in range(len(self.precio)):
            Precio+=self.precio[i]
        print("El precio total es: ",Precio)

    def CalcularPrecioxCantidad(self):
        ListaPrecioCantidad = []
        for i in range(len(self.precio)):
            PrecioxCantidad = self.precio[i] * self.cantidad[i]
            ListaPrecioCantidad.append(PrecioxCantidad)
        for x in range(len(ListaPrecioCantidad)):
            print(f"Elemento nro {x+1}: {self.elementos[x]} = {ListaPrecioCantidad[x]}")
class Empleado:
    def __init__(self,Rut = None,NombreCompleto = None,DiaNacimiento = None,MesNacimiento = None, AñoNacimiento = None,Usuario = None,Contraseña =None):
        self.rut = Rut
        self.nombre = NombreCompleto
        self.dia_nacimiento = DiaNacimiento
        self.mes_nacimiento = MesNacimiento
        self.año_nacimiento = AñoNacimiento
        self.usuario = Usuario
        self.contraseña = Contraseña
class Producto:
    def __init__(self,CodigoBarra = None,NombreProducto = None,CategoriaProducto = None,Marca = None,Precio = None,Cantidad = None,Stock = None):
        self.codigo = CodigoBarra
        self.nombre = NombreProducto
        self.categoria = CategoriaProducto
        self.marca = Marca
        self.precio = Precio
        self.cantidad = Cantidad
        self.stock = Stock

bod1 =Bodega(1,200,"Santa Maria","Nose")

empleado1 = Empleado("19.662.924-6","Richard",30,12,1998,"richard",12345)
empleado2 = Empleado("20.333.333-6","hola",12,3,2000,"hola",123456)
empleado3 =Empleado ("20.300.400-1","hofo",20,3,2001,"hofo",1234567)

producto1 =Producto(1,"Leche","Bebida","CocaCola",1000,2,4)
producto2 =Producto(2,"Agua","Nestle","Nestre",1200,6,10)
producto3 =Producto(3,"Leche","Bebida","CocaCola",500,8,43)
producto4 =Producto(4,"Leche","Bebida","CocaCola",1500,1,22)

bod1.AgregarElementos(producto1.nombre)
bod1.AgregarElementos(producto2.nombre)
bod1.AgregarElementos(producto3.nombre)
bod1.AgregarElementos(producto4.nombre)

bod1.AgregarPrecio(producto1.precio)
bod1.AgregarPrecio(producto2.precio)
bod1.AgregarPrecio(producto3.precio)
bod1.AgregarPrecio(producto4.precio)

bod1.AgregarCantidad(producto1.cantidad)
bod1.AgregarCantidad(producto2.cantidad)
bod1.AgregarCantidad(producto3.cantidad)
bod1.AgregarCantidad(producto4.cantidad)

bod1.MostrarElementosPrecioCantidad()
bod1.ContarElementos()
bod1.CalcularCantidad()
bod1.CalcularPrecio()
bod1.CalcularPrecioxCantidad()


usuarios = [empleado1,empleado2,empleado3]

logueado = False
while not logueado:
    usuario = input("Ingrese su usuario: ")
    contraseña = int(input("Ingrese su contraseña: "))
    for i in usuarios:
        if i.usuario == usuario and i.contraseña == contraseña:
            print("Inicio de sesion exitoso")
            opcion = int(input("Que quieres hacer?"))
            if opcion == 1:
                bod1.MostrarElementosPrecioCantidad()
            elif opcion == 2:
                bod1.ContarElementos()
            elif opcion == 3:
                bod1.CalcularCantidad()







