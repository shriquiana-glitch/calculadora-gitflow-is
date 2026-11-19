"""Calculadora básica de consola."""


def calculate(first_number: float, operator: str, second_number: float) -> float:
    """Realiza una operación aritmética básica."""
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        return first_number / second_number
    raise ValueError("Operación no válida. Usa +, -, * o /.")


def main() -> None:
    print("Calculadora básica")

    while True:
        try:
            first_number = float(input("Primer número: "))
            operator = input("Operación (+, -, *, /): ").strip()
            second_number = float(input("Segundo número: "))
            result = calculate(first_number, operator, second_number)
        except ValueError as error:
            print(f"Error: {error}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")
        else:
            print(f"Resultado: {result:g}")

        if input("¿Otra operación? (s/n): ").strip().lower() != "s":
            break


if __name__ == "__main__":
    main()
