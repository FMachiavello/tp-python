def domino():
    """ Devuelve todas las 28 fichas del domino
        . Este codigo separa la parte superior de la inferior para poder
         mostrar la ficha tradicional."""
    fichas_inferior = 0     # La parte inferior empieza en 0.
    for fichas_superior in range(0, 28):  # Recorre las 28 fichas.
        if fichas_superior <= 6:   # Las fichas del cero son 7.
            linea_uno = "     "  # Primera linea de numeros de la ficha.
            linea_dos = "     "  # Segunda linea de numeros de la ficha.
            linea_tres = "     "  # Tercera linea de numeros de la ficha.
            cantidad_fichas = 1
        elif fichas_superior <= 12:  # Las fichas del uno son 6.
            linea_uno = "     "
            linea_dos = "  0  "
            linea_tres = "     "
            cantidad_fichas = 2
        elif fichas_superior <= 17:  # Las fichas del dos son 5.
            linea_uno = "    0"
            linea_dos = "     "
            linea_tres = "0    "
            cantidad_fichas = 3
        elif fichas_superior <= 21:  # Las fichas del tres son 4.
            linea_uno = "    0"
            linea_dos = "  0  "
            linea_tres = "0    "
            cantidad_fichas = 4
        elif fichas_superior <= 24:  # Las fichas del cuatro son 3.
            linea_uno = "0   0"
            linea_dos = "     "
            linea_tres = "0   0"
            cantidad_fichas = 5
        elif fichas_superior <= 26:  # Las fichas del cinco son 2.
            linea_uno = "0   0"
            linea_dos = "  0  "
            linea_tres = "0   0"
            cantidad_fichas = 6
        elif fichas_superior == 27:  # Las fichas del seis es 1.
            linea_uno = "0 0 0"
            linea_dos = "     "
            linea_tres = "0 0 0"
            cantidad_fichas = 5
        print("╒═════╕")                # Muestra primera parte de la ficha.
        print("│" + linea_uno + "│")
        print("│" + linea_dos + "│")
        print("│" + linea_tres + "│")
        print("╞═════╡")
        if fichas_inferior == 0:
            linea_uno = "     "
            linea_dos = "     "
            linea_tres = "     "
        elif fichas_inferior == 1:
            linea_uno = "     "
            linea_dos = "  0  "
            linea_tres = "     "
        elif fichas_inferior == 2:
            linea_uno = "    0"
            linea_dos = "     "
            linea_tres = "0    "
        elif fichas_inferior == 3:
            linea_uno = "    0"
            linea_dos = "  0  "
            linea_tres = "0    "
        elif fichas_inferior == 4:
            linea_uno = "0   0"
            linea_dos = "     "
            linea_tres = "0   0"
        elif fichas_inferior == 5:
            linea_uno = "0   0"
            linea_dos = "  0  "
            linea_tres = "0   0"
        elif fichas_inferior == 6:
            linea_uno = "0 0 0"
            linea_dos = "     "
            linea_tres = "0 0 0"
        print("│" + linea_uno + "│")  # Muestra segunda parte de la ficha.
        print("│" + linea_dos + "│")
        print("│" + linea_tres + "│")
        print("╘═════╛")
        fichas_inferior = fichas_inferior + 1  # Recorre las fichas por numero.
        if fichas_inferior == 7:  # Cuando la cantidad de fichas llega a 7.
            fichas_inferior = 0 + cantidad_fichas   # Reduce las fichas x num.
domino()
