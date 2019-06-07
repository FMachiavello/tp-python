def sacarConsonantes(palabra):
    """Saca las consonantes de una palabra, recibiendo como parametro
    la palabra ingresada por el usuario normalizada a letras minusculas
    y devolviendo la palabra ingresada pero sin consonantes."""
    if type(palabra) not in [str]:
        raise TypeError("Ingrese una cadena adecuada")
    palabraLista = []
    for i, caracter in enumerate(palabra):
        if palabra[i] == "a":
            continue
        elif palabra[i] == "e":
            continue
        elif palabra[i] == "i":
            continue
        elif palabra[i] == "o":
            continue
        elif palabra[i] == "u":
            continue
        else:
            palabraLista.append(caracter)
        palabraFinal = "".join(palabraLista)
    return(palabraFinal[:])


def sacarVocales(palabra):
    """Saca las vocales de una palabra, recibiendo como parametro
    la palabra ingresada por el usuario normalizada a letras minusculas
    y devolviendo la palabra ingresada pero sin vocales."""
    if type(palabra) not in [str]:
        raise TypeError("Ingrese una cadena adecuada")
    palabraLista = []
    for i, caracter in enumerate(palabra):
        if palabra[i] == "a":
            palabraLista.append(caracter)
        elif palabra[i] == "e":
            palabraLista.append(caracter)
        elif palabra[i] == "i":
            palabraLista.append(caracter)
        elif palabra[i] == "o":
            palabraLista.append(caracter)
        elif palabra[i] == "u":
            palabraLista.append(caracter)
        else:
            continue
        palabraFinal = "".join(palabraLista)
    return(palabraFinal[:])


def adelantarVocal(palabra):
    """Adelanta las vocales de una palabra, recibiendo como parametro
    la palabra ingresada por el usuario normalizada a letras minusculas
    y devolviendo la palabra pero con sus vocales corridas y lugar
    hacia adelante."""
    if type(palabra) not in [str]:
        raise TypeError("Ingrese una cadena adecuada")
    palabraLista = []
    for i, caracter in enumerate(palabra):
        if palabra[i] == "a":
            palabraLista.append("e")
        elif palabra[i] == "e":
            palabraLista.append("i")
        elif palabra[i] == "i":
            palabraLista.append("o")
        elif palabra[i] == "o":
            palabraLista.append("u")
        elif palabra[i] == "u":
            palabraLista.append("a")
        else:
            palabraLista.append(caracter)
        palabraFinal = "".join(palabraLista)
    return(palabraFinal)


def esPalindromo(palabra):
    """Determina si una palabra es un palindromo o no ,recibiendo como parametro
    la palabra ingresada por el usuario normalizada a letras minusculas y
    devolviendo un true si la palabra es un palindromo
    o un false si no lo es."""
    if type(palabra) not in [str]:
        raise TypeError("Ingrese una cadena adecuada")
    palabra = palabra.replace(" ", "")
    if palabra[:: -1] == palabra:
        return True
    else:
        return False

if __name__ == "__main__":
    palabraIngresada = str(input("Ingrese una palabra "))
    palabraIngresadaNormalizada = str(palabraIngresada.casefold())
    sacarConsonantes(palabraIngresadaNormalizada)
    sacarVocales(palabraIngresadaNormalizada)
    adelantarVocal(palabraIngresadaNormalizada)
    esPalindromo(palabraIngresadaNormalizada)
