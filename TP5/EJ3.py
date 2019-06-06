def contDeVocales(cadena):
    if type(cadena) not in [str]:
        raise TypeError("Ingrese una cadena valida")
    cadena = cadena.casefold()
    v1 = cadena.count("a")
    v2 = cadena.count("e")
    v3 = cadena.count("i")
    v4 = cadena.count("o")
    v5 = cadena.count("u")
    v6 = cadena.count("á")
    v7 = cadena.count("é")
    v8 = cadena.count("í")
    v9 = cadena.count("ó")
    v10 = cadena.count("ú")
    vocal = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10
    if cadena == "":
        print("No se ha ingresado ninguna cadena")
        return("")
    elif vocal == 0:
        print("No se ha encontrado ninguna vocal")
        return("Nada")
    else:
        print("La cadena contiene", vocal, "vocal/es")
        return("Vocal")
