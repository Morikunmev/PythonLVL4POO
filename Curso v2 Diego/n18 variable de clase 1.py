class Cliente:
    suspendidos = []
    def __init__(self,codigo,nombre):
        self.codigo = codigo
        self.nombre = nombre
    def imprimir(self):
        print("Codigo: ",self.codigo)
        print("Nombre: ",self.nombre)
        self.esta_suspendido()
    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print()
    def suspender(self):
        Cliente.suspendidos.append(self.codigo)
cliente1 = Cliente(1234,"richard")
cliente2 = Cliente(2121,"carlos")
cliente3 = Cliente(2134,"juan")
cliente4 = Cliente(1311,"pedro")

cliente2.suspender()
cliente3.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)


