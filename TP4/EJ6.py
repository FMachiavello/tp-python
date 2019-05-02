import math
a = float(input("Ingrese el término cuadrático de la función: "))
b = float(input("Ingrese el término lineal de la función: "))
c = float(input("Ingrese el término independiente de la función: "))


def maxOMin(a, b, c):
    """Calcula el máximo o el mínimo de una función cuadrática. Recibe como
    parametro a,b y c de la funcion cuadratica , siendo estos el termino
    elevado al cuadrado , el termino con x y el termino que es solo
    un numero. Devuelve en pantalla el minimo o maximo
    de la funcion ingresada"""
    if a < 0:
        # Calcula el vertice en x de la funcion ingresada.
        xv = (-b/2*a)
        # Calcula el vertice en y de la funcion ingresada
        yv = a * xv + b * xv + c * xv
        # Muestra el maximo de la funcion.
        print("El máximo está en (", xv, ",", yv, ")")
    elif a > 0:
        # Muestra el maximo de la funcion.
        xv = (-b/2*a)
        # Calcula el vertice en y de la funcion ingresada.
        yv = a * xv + b * xv + c * xv
        # Muestra el minimo de la funcion.
        print("El mínimo está en (", xv, ",", yv, ")")
    else:
        # A no puede valer cero.
        print("El término cuadrático de la función no puede valer 0.")
maxOMin(a, b, c)

a = float(input("Ingrese el término cuadrático de la función: "))
b = float(input("Ingrese el término lineal de la función: "))
c = float(input("Ingrese el término independiente de la función: "))


def raices(a, b, c):
    """Calcula las raíces de una función cuadrática. Recibe como
    parametro a,b y c de la funcion cuadratica , siendo estos el termino
    elevado al cuadrado , el termino con x y el termino que es solo
    un numero. Devuelve en pantalla las raices de la funcion ingresada"""
    if a == 0:
        # Verifica que a no valga 0
        print("El coeficiente principal de la función no puede valer cero.")
    else:
        if (b ** 2) - (4 * a * c) < 0:
            # Verifica si la raiz queda de un numero negativo
            print("No tiene raíces.")
        elif (b ** 2) - (4 * a * c) > 0:
            # Verifica si la raiz es positiva
                raizuno = ((-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
                raizdos = ((-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
                print("Las raíces son {", raizdos, ",", raizuno, "}")
raices(a, b, c)

pendiente = float(input("Ingrese la pendiente de la primera función: "))
origen = float(input("Ingrese la ordenada origen de la primera función: "))
pendiente2 = float(input("Ingrese la pendiente de la segunda función: "))
origen2 = float(input("Ingrese la ordena origen de la segunda función: "))


def interseccion(pendiente, origen, pendiente2, origen2):
    """Calcula la interseccion entre dos funciones lineales.  Recibe como
    parametro a,b y c de la funcion cuadratica , siendo estos el termino
    elevado al cuadrado , el termino con x y el termino que es solo
    un numero. Devuelve en pantalla la interseccion de las rectas ingreadas"""
    if pendiente == pendiente2:
        # Se fija si las pendientes de ambas rectas son iguales
        print("Las rectas son paralelas.")
    else:
        # Calcula la interseccion entre las rectas
        resultadox = origen - origen2 / pendiente2 - pendiente
        resultadoy = pendiente * resultadox + orisgen
        print("La interseccion de las rectas se encuentra en",
              "(", resultadox,  ", ", resultadoy, ")")
interseccion(pendiente, origen, pendiente2, origen2)
