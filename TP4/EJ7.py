def dias(n):
    """Calcula en que día de la semana está la variable n segun el numero
    ingresado entre 1 y 366 para luego mostrarlo"""
    # Verifica si la variable es numerica
    if type(n) not in [int]:
        raise TypeError("No se puede calcular")
    # Verifica si esta dentro del rango
    if n < 1 or n > 366:
        raise ValueError("Numero fuera de rango")
    cont = 0
    if int(n) > 7:
        cont = int(n) // 7  # Devuelve la división entre n y 7 en num entero
    sem = int(n) - (7 * cont)  # Hace la ecuación para determinar que día es
    if sem == 1:
        print("Lunes")  # Si el numero obtenido es 1 muestra Lunes
        return(sem)
    elif sem == 2:
        print("Martes")  # Si el numero obtenido es 2 muestra Martes
        return(sem)
    elif sem == 3:
        print("Miércoles")  # Si el numero obtenido es 3 muestra Miércoles
        return(sem)
    elif sem == 4:
        print("Jueves")  # Si el numero obtenido es 4 muestra Jueves
        return(sem)
    elif sem == 5:
        print("Viernes")  # Si el numero obtenido es 5 muestra Viernes
        return(sem)
    elif sem == 6:
        print("Sábado")  # Si el numero obtenido es 6 muestra Sábado
        return(sem)
    elif sem == 7:
        print("Domingo")  # Si el numero obtenido es 7 muestra Domingo
        return(sem)
