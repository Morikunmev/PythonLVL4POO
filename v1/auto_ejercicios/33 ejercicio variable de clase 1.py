class Cliente:
    suspendido = []
    def __init__(self,codigo,nombre):
        self.codigo = codigo
        self.nombre = nombre
    def imprimir(self):
        print("Codigo: ",self.codigo)
        print("Nombre: ",self.nombre)
        self.esta_suspendido()
    def esta_suspendido(self):
        if self.codigo in Cliente.suspendido:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
    def suspender(self):
        Cliente.suspendido.append(self.codigo)
cliente1 = Cliente(1,"Carlos")
cliente2 = Cliente(2, "Ana")
cliente3 = Cliente(3,"Pedro")
cliente4 = Cliente(4,"Haddd")

cliente1.suspender()
cliente2.suspender()

cliente1.imprimir()