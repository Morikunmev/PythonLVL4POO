clientes= [{"Nombre":"Hector", "Apellidos":"Costa Guzman","Rut":"11111111-1"},
           {"Nombre":"Juan","Apellidos":"Gonzales Marquez","Rut":"22222222-2"}]
for cliente in clientes:
    print(f'"{cliente["Nombre"]},"{cliente["Apellidos"]}","{cliente["Rut"]}"')

def mostrar_cliente(clientes,dni):
    for c in clientes:
        if (dni==c["Rut"]):
            print("{} {}".format(c["Nombre"],c["Apellidos"]))
            return
    print("Cliente no encontrado")
mostrar_cliente(clientes,"11111111-1")
