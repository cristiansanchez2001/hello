from math import sqrt, nan


def suma(a="0", b="0"):
    """
    Funció que retorna la suma de a i b

    Entrada:
        a (int): valor de a
        b (int): valor de b

    Eixida:
        resultat (int) valor de a+b
    """
    return (a+b)


def resta(a="0", b="0"):
    """
    Funció que retorna la resta de a menys b

    Entrada:
        a (int): valor de a
        b (int): valor de b

    Eixida:
        resultat (int) valor de a-b
    """
    return (a-b)


def multiplicacio(a="0", b="0"):
    """
    Funció que retorna la multiplicació de a per b

    Entrada:
        a (int): valor de a
        b (int): valor de b

    Eixida:
        resultat (int) valor de a*b
    """
    return (a*b)


def divisio(a="0", b="1"):
    """
    Funció que retorna la divisió de a entre b

    Entrada:
        a (int): valor de a
        b (int): valor de b

    Eixida:
        resultat (int) valor de a/b
    """
    try:
        return (a/b)
    except ZeroDivisionError:
        return nan


def potencia(a="0", b="0"):
    """
    Funció que retorna la potència de a elevat a b

    Entrada:
        a (int): valor de a
        b (int): valor de b

    Eixida:
        resultat (int) valor de a**b
    """
    return (a**b)


def arrel_quadrada(a="0"):
    """
    Funció que retorna l'arrel quadrada de a

    Entrada:
        a (int): valor de a

    Eixida:
        resultat (int) valor de l'arrel quadrada de a
    """
    if(a < 0):
        return nan
    else:
        return (sqrt(a))


def factorial(a):
    """
    Funció que calcula el factorial de a

    Entrada:
        a (int): valor de a

    Eixida:
        resultat (int) valor de !a
    """
    if(a < 0):
        return nan
    elif(a == 0):
        return 1
    else:
        return a * factorial(a-1)
