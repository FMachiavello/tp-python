def milPalabras(palabra):
    """Muestra la variable palabra mil veces en una misma fila y
    con espacios"""
    # Detecta si es una palabra
    while palabra.isalpha() is False:
            palabra = input("Error, ingrese palabras o letras: ")
    for i in range(1, 1001):  # Recorre de 1 a 1000
        # print(palabra, end=" ") Muestra la palabra en una misma fila
        return (palabra + " ") * 1000
