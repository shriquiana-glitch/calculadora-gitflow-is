"""Prueba la interfaz sin depender de los módulos de los demás integrantes."""

from interfaz import iniciar_interfaz


def calcular_demo(operacion, a, b=None):
    """Función temporal para probar las operaciones desde la ventana."""
    if operacion == "+":
        return a + b
    if operacion == "-":
        return a - b
    if operacion == "*":
        return a * b
    if operacion == "/":
        if b == 0:
            raise ValueError("No se puede dividir entre cero.")
        return a / b
    if operacion == "**":
        return a**b
    if operacion == "raiz":
        if a < 0:
            raise ValueError("No se puede calcular la raíz de un número negativo.")
        return a**0.5
    raise ValueError("La operación seleccionada no es válida.")


def agregar_demo(historial, texto):
    """Guarda la operación y conserva solo las cinco más recientes."""
    historial.append(texto)
    if len(historial) > 5:
        del historial[:-5]


def listar_demo(historial):
    """Devuelve las operaciones recientes primero, sin exponer la lista original."""
    return list(reversed(historial))


def limpiar_demo(historial):
    """Vacía la lista recibida."""
    historial.clear()


if __name__ == "__main__":
    iniciar_interfaz(calcular_demo, agregar_demo, listar_demo, limpiar_demo)
