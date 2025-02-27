class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print("Se ha creado el alumno")
    def imprimir(self):
        print("Datos")
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)
    def condicional(self):
        if self.nota >=6.0:
            return "A aprobado"
        else:
            return "MAL"
    def __init__(self,nombre = None, nota = None):
        self.nombre = nombre
        self.nota = nota
        print("Se ha creado el alumno")

alumno1 = Alumno("Richard",6.0)
alumno1.imprimir()
resultado = alumno1.condicional()
print(resultado)