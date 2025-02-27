from abc import ABC, abstractmethod
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    @abstractmethod
    def calcular_perimetro(self):
        pass
class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado = lado
    def calcular_area(self):
        area = self.lado**2
        return area
    def calcular_perimetro(self):
        perimetro = 4 * self.lado
        return perimetro

cuadrado1 = Cuadrado(4)
print(f"el area del cuadrado es {cuadrado1.calcular_area()}")
print(f"El perimetro del cuadrado es {cuadrado1.calcular_perimetro()}")