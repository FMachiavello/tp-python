def filtro(cadena):
    c1 = cadena.split(' ')
    palabrasQueEmpiezanConA = []
    for c in c1:
        if c[0] == "a" or c[0] == "A":
            palabrasQueEmpiezanConA.append(c)
    print(" ".join(palabrasQueEmpiezanConA))
filtro("aca me gusta cagar")
