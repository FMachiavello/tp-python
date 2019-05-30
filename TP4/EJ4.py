import math
#lx = []
#ly = []
# for z in range(3):
#         if z == 2 and lx[0] == lx[1] and ly[0] == ly[1]:
#             print("La cordenada 1 coincide con la coordenada 2.")
#         x = input("Ingrese una coordenada x" + str(z + 1) + " >>> ")
#         if x.isnumeric() is False:
#             print("Ingrese solo numeros.")
#         else:
#             lx.append(x)
#         y = input("Ingrese una coordenada y" + str(z + 1) + " >>> ")
#         if y.isnumeric() is False:
#             print("Ingrese solo numeros.")
#         else:
#             ly.append(y)


def pitagoras(lx, ly):
    """Recibe 3 coordenadas guardadas en listas y mediante el teorema de pitágoras
     calcula el valor de la mas lejana al eje de coordenadas."""
    # if lx == "":
    #     raise TypeError("Lista 'lx' vacía.")
    # if ly == "":
    #     raise TypeError("Lista 'ly' vacía.")
    for y in range(0, 2):
        if lx[y] == "":
            raise ValueError("No se admiten cadenas vacías")
        if ly[y] == "":
            raise TypeError("No se admiten cadenas vacías")
        if type(ly[y]) not in [int, float]:
            raise TypeError("No se puede calcular")
        if type(lx[y]) not in [int, float]:
            raise TypeError("No se puede calcular")
    h1 = math.sqrt(float(lx[0])**2 + float(ly[0])**2)  # h1 es la hipotenusa1
    h2 = math.sqrt(float(lx[1])**2 + float(ly[1])**2)  # h2 es la hipotenusa2
    h3 = math.sqrt(float(lx[2])**2 + float(ly[2])**2)  # h3 es la hipotenusa3
    if lx[0] == lx[1] and ly[0] == ly[1]:
            if lx[1] == lx[2] and ly[1] == ly[2]:
                print("Todas las coordenadas son iguales.")
                print("No puedo calcular nada.")
    else:
<<<<<<< HEAD
        letra = "y"
    while not okey1:
        a = input("Ingrese una coordenada " + letra + "1 >>> ")
        if a.isnumeric() is False:
            print("Ingrese solo numeros.")
        else:
            l1.append(a)
            okey1 = True
    while not okey2:
        b = input("Ingrese una coordenada " + letra + "2 >>> ")
        if b.isnumeric() is False:
            print("Ingrese solo numeros.")
        else:
            l2.append(b)
            okey2 = True
    while not okey3:
        c = input("Ingrese una coordenada " + letra + "3 >>> ")
        if c.isnumeric() is False:
            print("Ingrese solo numeros.")
        else:
            l3.append(c)
            okey3 = True

pitagoras(l1, l2, l3)
=======
        if(h1 > h2 and h1 > h3):  # Compara si la hipotenusa1 es la mas lejana.
            print("la cordenada mas lejana es >>> (", lx[0], ";", ly[0], ")")
            return(lx[0], ly[0])
        elif(h2 > h1 and h2 > h3):  # Compara hipotenusa2.
            print("la cordenada mas lejana es >>> (", lx[1], ";", ly[1], ")")
            return(lx[1], ly[1])
        else:  # Por descarte la hipotenusa3 es la mas lejana.
            print("la cordenada mas lejana es >>> (", lx[2], ";", ly[2], ")")
            return(lx[2], ly[2])

>>>>>>> b82af1983a3b74358863fe88ab4b77db971b7afa
