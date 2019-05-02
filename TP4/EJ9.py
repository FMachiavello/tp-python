def evaluaciones(ejercicios, aprobar, correctas):
    """Determina si un alumno aprueba o no dependiendo de la info ingresada
    recibe como parametros los ejercicios que tiene la prueba, el
    porcentaje que necesita el alumno para aprobar y cuantos ejercicios
    realizo correctamente el alumno. Devuelve en pantalla si el alumno esta
    aprobado y el porcentaje de ejercicios correctos"""
    # Si se ingresa '*' el programa finaliza
    if ejercicios == "*":
        return
    elif aprobar == "*":
        return
    elif correctas == "*":
        return
    # Detecta si el dato es numerico
    while ejercicios.isnumeric() is False:
        ejercicios = input("(1°) ERROR, Ingrese un numero: ")

    while aprobar.isnumeric() is False:
        aprobar = input("(2°) ERROR, ingrese un numero: ")

    while correctas.isnumeric() is False:
        correctas = input("(3°) ERROR, ingrese un numero: ")
    # Correxión de var ejercicios
    while int(ejercicios) < 1:
        ejercicios = input("(1°) ERROR, Ingrese un dato valido: ")
        while ejercicios.isnumeric() is False:
            ejercicios = input("(1°) ERROR, Ingrese un numero: ")
        while int(ejercicios) < int(correctas):
            ejercicios = input("(1°) ERROR, Ingrese un dato valido: ")
    # Correxión de var aprobar
    while int(aprobar) < 1:
        aprobar = input("(2°) ERROR, Ingrese un dato valido: ")
        while aprobar.isnumeric() is False:
            aprobar = input("(2°) ERROR, ingrese un numero: ")
    while int(aprobar) > 100:
        aprobar = input("(2°) ERROR, Ingrese un dato valido: ")
        while aprobar.isnumeric() is False:
            aprobar = input("(2°) ERROR, ingrese un numero: ")
    # Correxión de var correctas
    while int(correctas) > int(ejercicios):
        correctas = input("(3°) ERROR, Ingrese un dato valido: ")
        while correctas.isnumeric() is False:
            correctas = input("(3°) ERROR, ingrese un numero: ")
    while int(correctas) < 0:
        correctas = input("(3°) ERROR, Ingrese un dato valido: ")
        while correctas.isnumeric() is False:
            correctas = input("(3°) ERROR, ingrese un numero: ")
    # Calcula el porcentaje de ejercicios correctos
    por = 100 * int(correctas) / int(ejercicios)
    # Muestra si estas aprobado dependiendo del porcentaje de referencia
    if por >= int(aprobar):
        print(round(por, 2), "%")
        print("Aprobado")
    # Muestra si estas desaprobado dependiendo del porcentaje de referencia
    elif por < int(aprobar):
        print(round(por, 2), "%")
        print("Desaprobado")
    # Vuelve a preguntar cuantos ej son correctos para seguir corrigiendo
    correctas = input("¿Cuántas son correctas?('*' finalizar): ")
    if correctas == "*":
        return
