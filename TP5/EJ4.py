def capitalize(cadena1, cadena2):
    """Detecta si la segunda palabra ingresada es la version capitalizada de
    la primera"""
    if type(cadena1) not in [str]:
        raise TypeError("Ingrese una cadena valida")
    if type(cadena2) not in [str]:
        raise TypeError("Ingrese una cadena valida")
    if cadena2 == cadena1.capitalize():
        print(True)
        return(True)
    else:
        print(False)
        return(False)
