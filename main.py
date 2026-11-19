from operaciones import calcular
from historial import agregar, listar, limpiar
from interfaz import iniciar_interfaz

if __name__ == "__main__":
    iniciar_interfaz(calcular, agregar, listar, limpiar)
