okey1 = False
while not okey1:
    a = input("Ingrese un número: ")
    if a.isnumeric() is False:
        print("Ingrese solo numeros.")
    elif a == "0":
        print("El numero no puede ser cero.")
    else:
        numero = int(a)
        okey1 = True


def MatrizIdentidad(dimension):
    """Calcula la matriz identidad de un numero. Recibiendo como parametro
        una cierta dimension y devolviendo en pantalla la matriz identidad
        de la dimension ingresada."""
    g = []  # Crea una lista.
    for i in range(0, dimension):
        g.append([0]*dimension)  # Crea una matriz.
        g[i][i] = 1  # Añade un uno en la posicion 1,1 2,2 y asi sucesivamente.
    for i in range(0, dimension):
        print(g[i])  # Muestra la matriz creada.
MatrizIdentidad(numero)
