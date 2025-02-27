class Motor:
    def __init__(self,motor = None):
        self.motor = motor
    def encender(self):
        print(f"Encendiendo el motor de tipo: {self.motor}")

class Coche:
    def __init__(self,marca = None, modelo= None):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("Gasolina")
    def arrancar(self):
        print(f"Arrancando el choche {self.marca} {self.modelo}")
        self.motor.encender()

coche1 = Coche()
coche1.arrancar()
