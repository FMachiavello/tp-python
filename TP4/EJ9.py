def evaluaciones(ejercicios, aprobar, correctas):
    """Determina si un alumno aprueba o no dependiendo de la info ingresada
    recibe como parametros los ejercicios que tiene la prueba, el
    porcentaje que necesita el alumno para aprobar y cuantos ejercicios
    realizo correctamente el alumno. Devuelve en pantalla si el alumno esta
    aprobado y el porcentaje de ejercicios correctos"""
    if not ejercicios[0] == "*":
        if type(ejercicios) not in [int, float]:
            raise TypeError("No se puede calcular")
    if not aprobar[0] == "*":
        if type(aprobar) not in [int, float]:
            raise TypeError("No se puede calcular")
    if not correctas[0] == "*":
        if type(correctas) not in [int, float]:
            raise TypeError("No se puede calcular")
    if ejercicios < 0 or correctas < 0 or aprobar < 1 or aprobar > 100:
        raise ValueError("No se pueden ingresar numeros negativos")
    # Si se ingresa '*' el programa finaliza
    if ejercicios == "*":
        return("Fin")
    elif aprobar == "*":
        return("Fin")
    elif correctas == "*":
        return("Fin")
    por = 100 * int(correctas) / int(ejercicios)
    # Muestra si estas aprobado dependiendo del porcentaje de referencia
    if por >= int(aprobar):
        print(round(por, 2), "%")
        print("Aprobado")
        return("Aprobado")
    # Muestra si estas desaprobado dependiendo del porcentaje de referencia
    elif por < int(aprobar):
        print(round(por, 2), "%")
        print("Desaprobado")
        return("Desaprobado")
    # Vuelve a preguntar cuantos ej son correctos para seguir corrigiendo
    correctas = input("¿Cuántas son correctas?('*' finalizar): ")
    if correctas == "*":
        return("Fin")
evaluaciones("*", "*", "*")
