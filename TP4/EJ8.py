def numRomanos(n):
    """Segun el numero ingresado en la variable n lo tansforma a numeros romanos
    devolviendo el mismo en pantalla"""
    # Correxión de la var n
    while n.isnumeric() is False:
        n = input("Error, ingrese un numero: ")
    while int(n) < 1:
        n = input("Ingrese un numero valido: ")
    while int(n) > 1000000:
        n = input("Ingrese un numero valido: ")
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
    # Muestra el numero 100000 hasta el 999999 en romanos
    elif int(n) >= 100000:
        print(cmil[cm] + dmil[dm] + mil[m] + cent[c] + dec[d] + unidad[u])
    # Muestra el numero 10000 hasta el 99999 en romanos
    elif int(n) >= 10000:
        print(dmil[dm] + mil[m] + cent[c] + dec[d] + unidad[u])
    # Muestra el numero 1000 hasta el 9999 en romanos
    elif int(n) >= 1000:
        print(mil[m] + cent[c] + dec[d] + unidad[u])
    # Muestra el numero 100 hasta el 999 en romanos
    elif int(n) >= 100:
        print(cent[c] + dec[c] + unidad[u])
    # Muestra el numero 10 hasta el 99 en romanos
    elif int(n) >= 10:
        print(dec[d] + unidad[u])
    # Muestra el numero 1 hasta el 9 en romanos
    else:
        print(unidad[int(n)])
