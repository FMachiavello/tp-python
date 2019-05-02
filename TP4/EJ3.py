def numTriangular(suma):
        """Calcula los numeros triangulares ingresados en la variable suma y
        los muestra"""
        while suma.isnumeric() is False:  # Detecta si el dato es numerico
                suma = input("Error, ingrese un numero: ")
        for i in range(1, int(suma) + 1):  # Recorre de 1 hasta el dato
                cont = i
                suma = int(suma) + cont
                print(cont, " - ", suma)  # Muestra los numeros triangulares
