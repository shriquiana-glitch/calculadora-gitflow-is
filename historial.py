"""Gestión del historial de operaciones en memoria."""


MAX_OPERACIONES = 5


def agregar(historial, texto):
    """Agrega una operación y conserva solo las cinco más recientes."""
    historial.append(texto)
    if len(historial) > MAX_OPERACIONES:
        del historial[:-MAX_OPERACIONES]


def listar(historial):
    """Devuelve una copia del historial, con lo más reciente primero."""
    return list(reversed(historial))


def limpiar(historial):
    """Vacía la lista de historial original."""
    historial.clear()
