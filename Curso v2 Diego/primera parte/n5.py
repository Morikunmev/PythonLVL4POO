class Libro:
    cantidad = 0
    libros = []
    def __init__(self,nombre = None):
        self.nombre = nombre
        Libro.cantidad+=1
        Libro.libros.append(self.nombre)
    def agregar_año(self,año = None):
        self.año = año
    def definir_estado(self,estado = None):
        self.estado = "en posesion" if estado is None or estado !="prestado" else "prestado"
    def imprimir(self):
        print("Nombre del libro: ",self.nombre)
        print("Año del libro: ",self.año)
        print("Estado del libro: ",self.estado)
class Biblioteca:
    def __init__(self):
        self.libro1 = Libro("1984")
        self.libro2 = Libro("matar un ruiseñor")
        self.libro3 = Libro("cien años de soledad")
    def operaciones_generales(self):
        self.libro1.agregar_año(1949)
        self.libro2.agregar_año(1960)
        self.libro3.agregar_año(1967)

        self.libro1.definir_estado("prestado")
        self.libro2.definir_estado("prestado")
        self.libro3.definir_estado("en posesion")

    def imprimir_todos(self):
        self.libro1.imprimir()
        self.libro2.imprimir()
        self.libro3.imprimir()
    def cantidad_general(self):
        print(f"El total hay {Libro.cantidad} libros registrados")

biblioteca1 = Biblioteca()
biblioteca1.operaciones_generales()
biblioteca1.imprimir_todos()
biblioteca1.cantidad_general()




