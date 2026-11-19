import unittest

from historial import agregar, limpiar, listar


class TestHistorial(unittest.TestCase):
    def test_lista_mas_recientes_primero(self):
        historial = ["1 + 1 = 2", "2 + 2 = 4"]
        self.assertEqual(listar(historial), ["2 + 2 = 4", "1 + 1 = 2"])

    def test_conserva_solo_cinco_operaciones(self):
        historial = []
        for numero in range(1, 8):
            agregar(historial, f"Operación {numero}")
        self.assertEqual(
            historial,
            ["Operación 3", "Operación 4", "Operación 5", "Operación 6", "Operación 7"],
        )

    def test_listar_devuelve_una_copia(self):
        historial = ["Primera", "Segunda"]
        copia = listar(historial)
        copia.clear()
        self.assertEqual(historial, ["Primera", "Segunda"])

    def test_limpiar_vacia_la_lista_original(self):
        historial = ["1 + 1 = 2"]
        limpiar(historial)
        self.assertEqual(historial, [])


if __name__ == "__main__":
    unittest.main()
