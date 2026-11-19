"""Operaciones aritméticas para la calculadora."""

import math


def calcular(operacion, a, b=None):
    """Calcula una operación y devuelve su resultado."""
    if operacion == "+":
        if b is None:
            raise ValueError("La suma necesita dos números.")
        return a + b
    if operacion == "-":
        if b is None:
            raise ValueError("La resta necesita dos números.")
        return a - b
    if operacion == "*":
        if b is None:
            raise ValueError("La multiplicación necesita dos números.")
        return a * b
    if operacion == "/":
        if b is None:
            raise ValueError("La división necesita dos números.")
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b
    if operacion == "**":
        if b is None:
            raise ValueError("La potencia necesita dos números.")
        resultado = a**b
        if isinstance(resultado, complex):
            raise ValueError("La potencia debe producir un resultado real.")
        return resultado
    if operacion == "raiz":
        if a < 0:
            raise ValueError("No se puede calcular la raíz de un número negativo.")
        return math.sqrt(a)
    raise ValueError("Operación no válida. Usa +, -, *, /, ** o raiz.")
