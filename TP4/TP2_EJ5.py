def volEsfera(x):
    import numpy as np
    if x == "":
        raise ValueError("No se admiten cadenas vacías")
    if type(x) not in [int, float]:
        raise TypeError("No se puede calcular")
    if x < 0:
        raise ValueError("No se admiten numeros negativos")
    volumen = round(4/3 * np.pi * x ** 3, 2)
    print("El volumen de la esfera es", volumen)
    return volumen
