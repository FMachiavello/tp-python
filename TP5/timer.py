def cuentaRegresiva(num):
    """Muestra en pantalla una cuenta regresiva que cambia dependiendo de la
        variable"""
    from time import sleep
    while num > 0:
        print(num)
        num = num - 1
        sleep(1)
