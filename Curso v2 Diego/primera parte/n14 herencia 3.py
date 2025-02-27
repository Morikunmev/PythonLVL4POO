class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    def imprimir(self):
        print(f"Marca del vehiculo: {self.marca}")
        print(f"Modelo del vehiculo: {self.modelo}")
class Coche(Vehiculo):
    def __init__(self,marca,modelo,puertas,pasajeros):
        super().__init__(marca,modelo)
        self.puertas = puertas
        self.pasajeros = pasajeros
    def imprimir(self):
        super().imprimir()
        print(f"Numero de puertas: {self.puertas}")
        print(f"Numero de pasajeros: {self.pasajeros}")
class Camioneta(Vehiculo):
    def __init__(self,marca,modelo,carga_maxima):
        super().__init__(marca,modelo)
        self.carga_maxima = carga_maxima
    def imprimir(self):
        super().imprimir()
        print(f"Carga maxima de la camioneta: {self.carga_maxima}")
coche1 = Coche("Ford","ford-escape",4,2)
coche1.imprimir()
