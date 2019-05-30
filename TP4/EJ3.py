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
