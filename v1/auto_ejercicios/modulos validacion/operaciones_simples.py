def suma(x1,x2):
    return x1+x2
def resta(x1,x2):
    return x1-x2
def multiplicacion(x1,x2):
    return x1*x2
def division(x1,x2):
    return x1/x2


def mayordef(x1,x2):
    if x1>x2:
        return x1
    else:
        return x2

def menordef(x1,x2):
    if x1<x2:
        return x1
    else:
        return x2

def dividirdef(x,y):
    try:
        dividir = x/y
        return dividir
    except ZeroDivisionError:
        return False
valor = dividirdef(4,-)
print(valor)

