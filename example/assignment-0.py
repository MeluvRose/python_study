def getNumber(a, b):
    if (a == None) | (b == None):
        return
    return True


def add(a=None, b=None):
    if not (getNumber(a, b)):
        return print("invalid input")
    print(a + b)


def sub(a=None, b=None):
    if not (getNumber(a, b)):
        return print("invalid input")
    print(a - b)


def mul(a=None, b=None):
    if not (getNumber(a, b)):
        return print("invalid input")
    print(a * b)


def div(a=None, b=None):
    if not (getNumber(a, b)):
        return print("invalid input")
    print(a / b)


def pow(a=None, b=None):
    if not (getNumber(a, b)):
        return print("invalid input")
    print(a**b)


a = 2

add(a)
sub(a)
mul(a)
div(a)
pow(a)

b = 3

add(a, b)
sub(a, b)
mul(a, b)
div(a, b)
pow(a, b)
