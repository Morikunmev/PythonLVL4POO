clientes= [{"Nombre":"Hector", "Apellidos":"Costa Guzman","Rut":"11111111-1"},
           {"Nombre":"Juan","Apellidos":"Gonzales Marquez","Rut":"22222222-2"}]
for cliente in clientes:
    print(f'"{cliente["Nombre"]},"{cliente["Apellidos"]}","{cliente["Rut"]}"')

def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if (dni ==c["Rut"]):
            del (clientes[i])
            print(str(c),"-->BORRADO")
            return
    print("Cliente no encontrado")
borrar_cliente(clientes,"22222222V")
borrar_cliente(clientes,"22222222-2")
print(clientes)
