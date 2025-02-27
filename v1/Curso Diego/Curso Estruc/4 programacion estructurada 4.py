lista=[]
while True:
    sabor = input("De que sabor es la galleta?: ")
    tamaño = input("De que tamaño en la galleta?: ")
    galleta = "Sabor: " + sabor + " Tamaño: " + tamaño
    lista.append(galleta)
    print()
    for i in range(len(lista)):
        print(f"galleta {i+1}: {lista[i]})")
