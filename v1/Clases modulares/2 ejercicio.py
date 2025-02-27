from Validacion import generaldef as val

class Producto:
    def __init__(self):
        self.nombre=val.string_nombre("Ingresa el nombre del producto: ")
        self.precio=val.preciodef("Ingresa el precio del producto: ")
        self.cantidad=val.enterodef("Ingresa la cantidad del producto: ")
    def imprimir(self):
        print("Producto nombre: ",self.nombre)
        print("Precio producto: ",self.precio)
        print("Cantidad producto: ",self.cantidad)
    def calculo(self):
        importe=self.precio*self.cantidad
        print("Debe pagar: " +str(importe))

producto1=Producto()
producto1.imprimir()
producto1.calculo()
        
