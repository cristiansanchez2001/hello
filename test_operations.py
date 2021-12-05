import operations


def test_suma():
    assert operations.suma(3, 3) == 6
    assert operations.suma(0, 0) == 0
    assert operations.suma(-5, -6) == -11
    assert operations.suma(5, -6) == -1


def test_resta():

    assert operations.resta(4, 2) == 2


def test_multi():
    assert operations.multiplicacio(5, 4) == 20


def test_divi():

    assert operations.divisio(6, 2) == 3


def test_arrel():
    assert operations.arrel_quadrada(9) == 3


def test_factorial():
    assert operations.factorial(3) == 6
    pass
