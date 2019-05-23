def numTriangular(n):
    """Calcula los numeros triangulares ingresados en la variable suma y
    los muestra"""
    # Determina si es posible calcular el numero.
    if type(n) not in [int, float]:
        raise TypeError("No se puede calcular")
    s = []
    c = []
    for i in range(1, int(n) + 1):  # Recorre de 1 hasta el dato
        cont = i
        suma = int(cont) * (int(cont) + 1) / 2
        c.append(cont)
        s.append(suma)
        print(cont, " - ", suma)  # Muestra los numeros triangulares
    return(c, s)
numTriangular("a")
