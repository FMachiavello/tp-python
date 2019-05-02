def dias(n):
    """Calcula en que día de la semana está la variable n segun el numero
    ingresado entre 1 y 366 para luego mostrarlo"""
    while n.isnumeric() is False:  # Detecta si el dato es numerico
        n = input("Error, ingrese un numero: ")
    cont = 0
    if int(n) > 7:
        cont = int(n) // 7  # Devuelve la división entre n y 7 en num entero
    sem = int(n) - (7 * cont)  # Hace la ecuación para determinar que día es
    if int(n) <= 366 and int(n) > 0:  # Permite ingresar numeros del 1 al 366
        if sem == 1:
            print("Lunes")  # Si el numero obtenido es 1 muestra Lunes
        elif sem == 2:
            print("Martes")  # Si el numero obtenido es 2 muestra Martes
        elif sem == 3:
            print("Miércoles")  # Si el numero obtenido es 3 muestra Miércoles
        elif sem == 4:
            print("Jueves")  # Si el numero obtenido es 4 muestra Jueves
        elif sem == 5:
            print("Viernes")  # Si el numero obtenido es 5 muestra Viernes
        elif sem == 6:
            print("Sábado")  # Si el numero obtenido es 6 muestra Sábado
        elif sem == 7:
            print("Domingo")  # Si el numero obtenido es 7 muestra Domingo
    else:
        print("Numero incorrecto")
        return
