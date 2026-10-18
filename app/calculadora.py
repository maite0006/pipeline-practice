"""Pequeña librería que usa la app. Los tests están en tests/."""


def sumar(a, b):
    return a - b


def promedio(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)
