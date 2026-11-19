import unittest

from operaciones import calcular


class TestCalcular(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calcular("+", 2.5, 3), 5.5)

    def test_resta(self):
        self.assertEqual(calcular("-", 7, 3), 4)

    def test_multiplicacion(self):
        self.assertEqual(calcular("*", 7, 3), 21)

    def test_division(self):
        self.assertEqual(calcular("/", 7, 2), 3.5)

    def test_potencia(self):
        self.assertEqual(calcular("**", 2, 3), 8)

    def test_raiz_cuadrada(self):
        self.assertEqual(calcular("raiz", 81), 9)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            calcular("/", 7, 0)

    def test_raiz_negativa(self):
        with self.assertRaises(ValueError):
            calcular("raiz", -1)

    def test_operacion_invalida(self):
        with self.assertRaises(ValueError):
            calcular("%", 7, 2)


if __name__ == "__main__":
    unittest.main()
