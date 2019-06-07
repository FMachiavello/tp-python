def primeraLetra(cadena):
    """Muesta la primera letra de cada palabra"""
    if type(cadena) not in [str]:
        raise TypeError("Ingrese una cadena correcta")
    cadenaSplit = cadena.split(' ')
    letra = ""
    for c in cadenaSplit:
        letra += c[0]
    print("(a) ", letra)
    return("OK (a)")


def letraMayuscula(cadena):
    """Muestra las primera letra de cada palabra en mayuscula"""
    if type(cadena) not in [str]:
        raise TypeError("Ingrese una cadena correcta")
    cadenaTitle = cadena.title()
    print("(b) ", cadenaTitle)
    return("OK (b)")


def palabrasConA(cadena):
    """Muestra las palabras con 'A' que se ingresaron en la cadena"""
    if type(cadena) not in [str]:
        raise TypeError("Ingrese una cadena correcta")
    palabrasA = []
    cadenaSplit = cadena.split(' ')
    for c in cadenaSplit:
        if c[0] == "a" or c[0] == "A":
            palabrasA.append(c)
    print("(c) ", " ".join(palabrasA))
    if len(palabrasA) == 0:
        return("Fail (c)")
    return("OK (c)")
