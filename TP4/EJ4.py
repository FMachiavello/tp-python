import math
l1 = []
l2 = []
l3 = []


def pitagoras(l1, l2, l3):
    """Recibe 3 coordenadas guardadas en listas y mediante el teorema de pitágoras
     calcula el valor de la mas lejana al eje de coordenadas."""
    h1 = math.sqrt(float(l1[0])**2 + float(l1[1])**2)  # h1 es la hipotenusa1
    h2 = math.sqrt(float(l2[0])**2 + float(l2[1])**2)  # h2 es la hipotenusa2
    h3 = math.sqrt(float(l3[0])**2 + float(l3[1])**2)  # h3 es la hipotenusa3
    if(h1 > h2 and h1 > h3):  # Compara si las hipotenusa1 es la mas lejana.
        print("la cordenada mas lejana es (", l1[0], ";", l1[1], ")")
    elif(h2 > h1 and h2 > h3):  # Compara si las hipotenusa2 es la mas lejana.
        print("la cordenada mas lejana es (", l2[0], ";", l2[1], ")")
    else:  # Por descarte la hipotenusa3 es la mas lejana.
        print("la cordenada mas lejana es >>> (", l3[0], ";", l3[1], ")")
for i in range(2):
    okey1 = False
    okey2 = False
    okey3 = False
    if i == 0:
        letra = "x"
    else:
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
