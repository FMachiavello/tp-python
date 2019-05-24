def perRectangulo(a, b):
    if a < 0 or b < 0:
        raise ValueError("No se pueden calcular numeros negativos")
    if type(a) not in [int, float, complex]:
        raise TypeError("No se puede calcular")
    if type(b) not in [int, float, complex]:
        raise TypeError("No se puede calcular")
    perimetro = (a + b) * 2
    print("El perimetro es:", perimetro)
    return(perimetro)
