import getpass
from timer import cuentaRegresiva


def contraseña(passw):
    code = "Luna"
    while passw != code:
        n = 5
        for i in range(1, n + 1):
            cont = n - (i - 1)
            if cont == 5:
                print(False)
                num = 5
                cuentaRegresiva(num)
                passw = getpass.getpass("CONTRASEÑA:")
                if passw == code:
                    print(True)
                    return(True)
            elif cont == 4:
                print(False)
                num = 10
                cuentaRegresiva(num)
                passw = getpass.getpass("CONTRASEÑA:")
                if passw == code:
                    print(True)
                    return(True)
            elif cont == 3:
                print(False)
                num = 15
                cuentaRegresiva(num)
                passw = getpass.getpass("CONTRASEÑA:")
                if passw == code:
                    print(True)
                    return(True)
            elif cont == 2:
                print(False)
                num = 20
                cuentaRegresiva(num)
                passw = getpass.getpass("CONTRASEÑA:")
                if passw == code:
                    print(True)
                    return(True)
            else:
                print(False)
                num = 25
                cuentaRegresiva(num)
                passw = getpass.getpass("CONTRASEÑA:")
                if passw == code:
                    print(True)
                    return(True)
        print("Ha superado el limite de intentos")
        return(False)
    print(True)
    return(True)
