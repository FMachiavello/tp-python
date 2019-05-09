def numTriangular(n):
        """Calcula los numeros triangulares ingresados en la variable suma y
        los muestra"""
        if n.isnumeric() is False:  # Detecta si el dato es numerico
                return None
        for i in range(1, int(n) + 1):  # Recorre de 1 hasta el dato
                cont = i
                suma = int(cont) * (int(cont) + 1) / 2
                print(cont, " - ", suma)  # Muestra los numeros triangulares
                return(int(n) * (int(n) + 1) / 2)

if __name__ == '__main__':
        numTriangular(4)
