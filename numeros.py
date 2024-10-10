def turno_farmacia():
    for turno in range(1, 10000):
        yield f"          F {turno}"


def turno_perfume():
    for turno in range(1, 10000):
        yield f"          P {turno}"


def turno_cosme():
    for turno in range(1, 10000):
        yield f"          C {turno}"


f = turno_farmacia()
p = turno_perfume()
c = turno_cosme()


def funcion_decoradora(func):
    def wrapper():
        print("**************************")
        print("      Su turno es: ")
        func()
        print(" Aguarde y sera atendido.")
        print("**************************")
    return wrapper


@funcion_decoradora
def siguiente_f():
    print(next(f))


@funcion_decoradora
def siguiente_p():
    print(next(p))


@funcion_decoradora
def siguiente_c():
    print(next(c))