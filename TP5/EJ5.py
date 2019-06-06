def filtro(cadena):
    if type(cadena) not in [str]:
        raise TypeError("Ingrese una cadena correcta")
    cadenaSplit = cadena.split(' ')
    letra = ""
    for c in cadenaSplit:
        letra += c[0]
    print("(a) ", letra)
    cadenaTitle = cadena.title()
    print("(b) ", cadenaTitle)
    palabrasA = []
    for c in cadenaSplit:
        if c[0] == "a" or c[0] == "A":
            palabrasA.append(c)
    print("(c) ", " ".join(palabrasA))
    if len(palabrasA) == 0:
        return("Fail (c)")
    return("OK")
