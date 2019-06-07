noSeEncontroElNombreEnLaAgenda = bool
Agenda = {}
Agenda = {'Pepe': '1136485968', 'Tito': '1137569120', 'Luis': '1187954231'}
nombreRegistrado = str


def ingresaNuevoNumero(nombre):
    """Pide que ingreses un número mayor a 8 dígitos para validarlo."""
    nombreRegistrado = nombre  # Pasa a la variable el nombre traído.
    okey = bool
    okey = True
    while okey is True:  # Sigue pidiendo el número si es mal ingresado.
        telefono = input("Ingrese un número: ")
        if not len(telefono) >= 8:
            print("Debe ingresar un nÚmero mayor a 8 dígitos")
        else:
            Agenda[nombreRegistrado] = telefono
            okey = False


def testing(nombre):
    """Se fija si se encontró el nombre recibido en la agenda
       y si no agregarlo. Y tambien se pregunta si el número ya guardado en
       el diccionario es correcto, y si no, cambiarlo."""
    nombreRegistrado = nombre   # Pasa a la variable el nombre traído.
    if __name__ == "__main__":  # ESTO LO DISCUTIMOS. MI SOLUCIÓN FUE
                                # ESTA (ENTENDÍ TU PUNTO).
        if noSeEncontroElNombreEnLaAgenda is True:
            ingresaNuevoNumero(nombreRegistrado)
        else:
            cambiarNumeroIngresado = str
            respuestaEsperada = bool
            respuestaEsperada = False
            pregunta = input("¿Desea cambiar el número" +
                             " registrado? (S/N): ")
            cambiarNumeroIngresado = pregunta.upper()
            while respuestaEsperada is False:   # Repite el procedimiento.
                                                # hasta recibir una s o una n.
                if cambiarNumeroIngresado == "S":
                    respuestaEsperada = True
                    ingresaNuevoNumero(nombreRegistrado)
                elif cambiarNumeroIngresado == "N":
                    respuestaEsperada = True
                    break
                else:
                    print("Ingrese una respuesta esperada (S/N).")
                    pregunta = input("¿Desea cambiar el número" +
                                     " registrado? (S/N): ")
                    cambiarNumeroIngresado = pregunta.upper()


def agenda(nombre):
    nombreRegistrado = nombre
    letras = ['a', 'á', 'b', 'c', 'd', 'e', 'é', 'f', 'g', 'h', 'i', 'í',
              'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'ó', 'p',
              'q', 'r', 's', 't', 'u', 'ú', 'v', 'w',
              'x', 'y', 'z']
    while True:
        try:
            if nombre == "":
                raise ValueError("No se admiten cadenas vacías")
            for y in range(0, len(nombre)):
                if nombre[0 + y].lower() not in letras:
                    raise TypeError("Ingrese una cadena válida.")
            else:
                noSeEncontroElNombreEnLaAgenda = False
                testing(nombreRegistrado)
                numero = print(Agenda[nombreRegistrado])
                return numero
                break
        except(KeyError):
            noSeEncontroElNombreEnLaAgenda = True
            testing(nombreRegistrado)
            raise TypeError("No se ha encontrado el nombre en la agenda.")
            break


if __name__ == "__main__":
    nombreIngresado = str
    while nombreIngresado != "*":
        nombre = input("Ingrese un nombre para buscar el contacto: ")
        nombreIngresado = nombre.capitalize()
        if nombreIngresado == "*":
            print("Cerrando programa.")
            break
        agenda(nombreIngresado)