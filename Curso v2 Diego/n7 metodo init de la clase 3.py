class Cuadrado:
    def __init__(self,lado):
        self.lado = lado
    def mostrar_perimetro(self):
        perimetro = self.lado * 4
        print(f"el perimetro del cuadrado es: {perimetro}")
    def mostrar_superficie(self):
        superficie = self.lado * self.lado
        print("La superficie del cuadrado es: ",superficie)

#perimetro no le agregamos el indicador self porque no lo queremos definir como un atributo de la clase
#es una variable local al metodo "mostrar_perimetro"
#en otro metodo a esa variable perimetro no lo puedo acceder
#pero si se puede acceder en otro metodo al atributo lado, ya que le antecedemos el indicador self