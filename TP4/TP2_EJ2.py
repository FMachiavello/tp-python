def areaRectangulo(altura2, base2):
    if altura2 < 0 or base2 < 0:
        raise ValueError("No es posible calcular numeros negativos")
    if type(altura2)not in [int, float, complex]:
        raise TypeError("No es posible calcular")
    if type(base2) not in [int, float, complex]:
        raise TypeError("No es posible calcular")
    area = float(altura2) * float(base2)
    print("El área es:", area)
    return(area)
