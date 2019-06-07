import getpass
from timer import cuentaRegresiva


def contraseña(passw):
    """Permite ingresar una contraseña establecida. Hasta que no se haya ingresado
    correctamente el programa no finlaiza"""
    code = "Luna"  # Contraseña
    while passw != code:
        n = 5
        for i in range(1, n + 1):
            cont = n - (i - 1)
            if cont == 5:
                cuentaRegresiva(5)
                print("Quedan 5 intentos")
                passw = getpass.getpass("CONTRASEÑA:")
                if passw == code:
                    print(True)
                    return(True)
            elif cont == 4:
                cuentaRegresiva(10)
                print("Quedan 4 intentos")
                passw = getpass.getpass("CONTRASEÑA:")
                if passw == code:
                    print(True)
                    return(True)
            elif cont == 3:
                cuentaRegresiva(15)
                print("Quedan 3 intentos")
                passw = getpass.getpass("CONTRASEÑA:")
                if passw == code:
                    print(True)
                    return(True)
            elif cont == 2:
                cuentaRegresiva(20)
                print("Quedan 2 intentos")
                passw = getpass.getpass("CONTRASEÑA:")
                if passw == code:
                    print(True)
                    return(True)
            else:
                cuentaRegresiva(25)
                print("Queda 1 intento")
                passw = getpass.getpass("CONTRASEÑA:")
                if passw == code:
                    print(True)
                    return(True)
        print("Ha superado el limite de intentos")
        return
    print(True)
    return(True)
