def perCirculo(radio):
    if type(radio) not in [int, float]:
        raise TypeError("No se puede calcular")
    if radio < 0:
        raise ValueError("No se puede calcular")
    perimetro = 2 * 3.141516 * float(radio)
    print("El perimetro es:", perimetro)
    return perimetro


def areaCirculo(radio):
    if type(radio) not in [int, float]:
        raise TypeError("No se puede calcular")
    if radio < 0:
        raise ValueError("No se puede calcular")
    area = (3.141516 * float(radio)) ** 2
    print("El área es:", area)
    return area
