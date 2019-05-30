def isnumeric(n):
    if str(type(n)) == "<class 'int'>" or str(type(n)) == "<class 'float'>" or str(type(n)) == "<class 'complex'>":
        return True
    else:
        return False
