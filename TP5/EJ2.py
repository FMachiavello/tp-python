def contDeLetras(cadena):
    """Determina si en la cadena ingresada hay mas letras 'A' o letras 'B'"""
    if type(cadena) not in [str]:
        raise TypeError("Ingrese una cadena valida")
    cadena = cadena.casefold()
    l1 = cadena.count("a")
    l2 = cadena.count("á")
    l3 = cadena.count("e")
    l4 = cadena.count("é")
    letraA = l1 + l2
    letraB = l3 + l4
    if cadena == "":
        print("No se ha ingresado ninguna cadena")
        return("")
    elif letraA == 0 and letraB == 0:
        print("No se ha ingresado ninguna letra 'A' ni 'E'")
        return("Nada")
    elif letraA == letraB:
        print("La cadena tiene la misma cantidad de letras 'A' y 'E'")
        return("Igual")
    elif letraA > letraB:
        print("La cadena tiene más letras 'A' que 'E'")
        return("A")
    else:
        print("La cadena tiene más letras 'E' que 'A'")
        return("E")
