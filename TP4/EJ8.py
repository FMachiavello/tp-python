def numRomanos(n):
    """Segun el numero ingresado en la variable n lo tansforma a numeros romanos
    devolviendo el mismo en pantalla"""
    # Verifica si la variable es numerica
    if type(n) not in [int]:
        raise TypeError("No se puede calcular")
    # Verifica si esta dentro del rango
    if n < 1 or n > 1000000:
        raise ValueError("Numero fuera de rango")
    unidad = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    dec = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    cent = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    mil = ["", "M", "MM", "MMM", "IV/", "V/", "VI/", "VII/", "VIII/", "IX/"]
    dmil = ["", "X/", "XX/", "XXX/", "XL/", "L/", "LX/", "LXX/", "LXXX/", """
    XC/"""]
    cmil = ["", "C/", "CC/", "CCC/", "CD/", "D/", "DC/", "DCC/", "DCCC/", """
    CM/"""]
    # Calcula la posicion en la lista segun el numero
    u = int(n) % 10
    d = int(n) // 10 % 10
    c = int(n) // 100 % 10
    m = int(n) // 1000 % 10
    dm = int(n) // 10000 % 10
    cm = int(n) // 100000
    # Muestra el numero 1000000 en romanos
    if int(n) == 1000000:
        print("M//")
        return("M//")
    # Muestra el numero 100000 hasta el 999999 en romanos
    elif int(n) >= 100000:
        print(cmil[cm] + dmil[dm] + mil[m] + cent[c] + dec[d] + unidad[u])
        return(cmil[cm] + dmil[dm] + mil[m] + cent[c] + dec[d] + unidad[u])
    # Muestra el numero 10000 hasta el 99999 en romanos
    elif int(n) >= 10000:
        print(dmil[dm] + mil[m] + cent[c] + dec[d] + unidad[u])
        return(dmil[dm] + mil[m] + cent[c] + dec[d] + unidad[u])
    # Muestra el numero 1000 hasta el 9999 en romanos
    elif int(n) >= 1000:
        print(mil[m] + cent[c] + dec[d] + unidad[u])
        return(mil[m] + cent[c] + dec[d] + unidad[u])
    # Muestra el numero 100 hasta el 999 en romanos
    elif int(n) >= 100:
        print(cent[c] + dec[c] + unidad[u])
        return(cent[c] + dec[c] + unidad[u])
    # Muestra el numero 10 hasta el 99 en romanos
    elif int(n) >= 10:
        print(dec[d] + unidad[u])
        return(dec[d] + unidad[u])
    # Muestra el numero 1 hasta el 9 en romanos
    else:
        print(unidad[int(n)])
        return(unidad[int(n)])
