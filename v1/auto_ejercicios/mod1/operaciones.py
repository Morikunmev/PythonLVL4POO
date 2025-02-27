def mayordef(x):
    if x>=18:
        return True
    else:
        return False
def promediodef(a,q,e,r):
    promedio = a+q+e+r /4
    return promedio

def mayorpromediodef(Luchador):
    MayorPromedio = max(Luchador.ListaPromedio)
    IndicePromedio = Luchador.ListaPromedio.index(MayorPromedio)
    NombreMayor = Luchador.ListaNombre[IndicePromedio]
    print("El mayor promedio es de : ",NombreMayor)
    print("Que corresponde a: ",MayorPromedio)
def menorpromediodef(Luchador):
    MenorPromedio = min(Luchador.ListaPromedio)
    IndicePormedio = Luchador.ListaPromedio.index(MenorPromedio)
    MenorNombre = Luchador.ListaNombre[IndicePormedio]
    print("El menor promedio es de : ",MenorNombre)
    print("Que corresponde a: ",MenorPromedio)

#Listado de juego y luchadores
def IteracionJuego(Juego):
    for i in range(len(Juego.ListaNombre)):
        print(f"Registro nro {i+1}, Nombre: {Juego.ListaNombre[i]}, Version: {Juego.ListaVersion[i]}")
def IteracionLuchador(Luchador):
    for i in range(len(Luchador.ListaNombre)):
        print(f"Registro nro {i + 1}: Nombre: {Luchador.ListaNombre[i]}, Promedio de estadistica: {Luchador.ListaPromedio[i]}")

#Datos de atributos de instancia
def Estadisticas(nombre,fuerza,destreza,resistencia,velocidad):
    print(f"Nombre: {nombre}")
    print(f"Fuerza: {fuerza}")
    print(f"Destreza: {destreza}")
    print(f"Resistencia: {resistencia}")
    print(f"Velocidad: {velocidad}")
def DatosJuego(nombre,version):
    print(f"Nombre Juego: {nombre}")
    print(f"Version Juego: {version}")
