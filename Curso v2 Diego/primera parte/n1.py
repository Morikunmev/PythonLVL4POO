class Estudiante:
    def __init__(self,nombre= None,edad = None):
        self.nombre = nombre.capitalize()
        self.edad = edad
        self.notas = []
        self.promedio = None
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Promedio de notas: ",self.promedio)
    def agregar_nota(self,nota):
        self.notas.append(nota)
    def calcular_promedio(self):
        suma = 0
        for i in self.notas:
            suma+=i
        self.promedio = suma // len(self.notas)
    def encontrar_maximo(self):
        maximo = 0
        minimo = self.notas[0]
        for i in self.notas:
            if i>maximo:
                maximo = i
            elif i<minimo:
                minimo = i
        print(f"La nota maxima es: {maximo} ")
        print(f"La nota minima es: {minimo}")
estudiante1 = Estudiante("richard",24)
estudiante1.agregar_nota(7.0)
estudiante1.agregar_nota(7.0)
estudiante1.agregar_nota(5.0)
estudiante1.agregar_nota(3.0)
estudiante1.calcular_promedio()
estudiante1.imprimir()
estudiante1.encontrar_maximo()