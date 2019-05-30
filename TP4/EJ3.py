<<<<<<< HEAD
from FIN import isnumeric


def numTriangular(n):
        """Calcula los numeros triangulares ingresados en la variable suma y
        los muestra"""
        if not isnumeric(n):
                return "Todo mal"  # Detecta si el dato es numerico
        for i in range(1, int(n) + 1):  # Recorre de 1 hasta el dato
                cont = i
                suma = int(cont) * (int(cont) + 1) / 2
                print(cont, " - ", suma)  # Muestra los numeros triangulares
                return(int(n) * (int(n) + 1) / 2)
=======
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
>>>>>>> b82af1983a3b74358863fe88ab4b77db971b7afa
