def areaRec(a, b, c, d):
    if type(a) not in [int]:
        raise TypeError("No se puede calcular")
    if type(b) not in [int]:
        raise TypeError("No se puede calcular")
    if type(c) not in [int]:
        raise TypeError("No se puede calcular")
    if type(d) not in [int]:
        raise TypeError("No se puede calcular")
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    for i in range(2):
        c1.append(a)
        c2.append(b)
        c3.append(c)
        c4.append(d)
    ba = float(c2[0]) - float(c1[0])
    al = float(c4[1]) - float(c1[1])
    if ba < 0:
        base3 = float(ba) * -1
    if al < 0:
        altura3 = float(al) * -1
    area2 = ba * al
    print(area2)
    return area2
