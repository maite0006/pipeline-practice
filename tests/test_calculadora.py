from app.calculadora import sumar, promedio


def test_sumar():
    assert sumar(2, 3) == 5


def test_promedio():
    assert promedio([4, 6, 8]) == 6


def test_promedio_vacio():
    assert promedio([]) == 0
