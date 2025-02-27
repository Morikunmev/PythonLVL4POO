class Motor:
    def __init__(self,tipo):
        self.tipo = tipo
    def encender(self):
        print(f"Encendiendo el motor de tipo {self.tipo}")

class Coche:
    def __init__(self,marca =None,modelo = None):
        self.marca =marca
        self.modelo = modelo
        self.motor = Motor("Gasolina")
    def arrancar(self):
        print(f"Arrancando el coche {self.marca} {self.modelo}")
        self.motor.encender()
coche1 =Coche()

