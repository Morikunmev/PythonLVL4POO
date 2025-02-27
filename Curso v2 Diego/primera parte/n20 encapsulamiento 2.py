class Persona:
    def __init__(self,nombre,edad,direccion):
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion
    def getdireccion(self):
        return self.__direccion
    def setdireccion(self,nuevo):
        self.__direccion = nuevo
        print(f"Direccion cambiada {self.__direccion}")
    def setedad(self,nuevo):
        if type(nuevo) == int:
            if nuevo>15:
                self.__edad = nuevo
                print(f"Edad cambiada con exito: {self.__edad}")
            else:
                print("No puede ingresar una edad menor a 15 años")
        else:
            print("Tienes que ingresar un numero entero")
    def setnombre(self,nuevo):
        if type(nuevo) == str and not any(i.isnumeric() for i in nuevo):
            self.__nombre = nuevo
            print(f"Nombre cambiado con exito: {self.__nombre}")


persona1 = Persona("Richard",24,"Santa Maria")
print(f"La direccion es {persona1.getdireccion()}")
persona1.setdireccion("Villa Alemana")
persona1.setedad(18)
persona1.setnombre("richard")