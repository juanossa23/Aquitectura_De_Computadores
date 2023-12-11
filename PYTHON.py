# Función para convertir un número de una base a otra
def convert(from_base, to_base, number):
    try:
        # Convertir el número a entero en la base original
        number_int = int(number, from_base)
        # Convertir el número a la base deseada y ponerlo en mayúsculas
        result = str(number_int).upper()
    except ValueError:
        result = "Error de conversión. Verifique los números ingresados."
    return result

# Función para calcular el resultado de una operación lógica
def calculate(input_a, input_b, operation):
    if not (input_a in ["0", "1"] and input_b in ["0", "1"]):
        print("Por favor, ingrese solo valores 0 o 1.")
        return

    result = None
    if operation == "and":
        result = input_a & input_b
    elif operation == "or":
        result = input_a | input_b
    elif operation == "xor":
        result = input_a ^ input_b

    if result is not None:
        print(f"Resultado: {result}")

# Programa principal
from_base = int(input("Base de origen: "))
to_base = int(input("Base de destino: "))
number = input("Número: ")

result = convert(from_base, to_base, number)
print(f"Resultado: {result}")

# Simular puertas lógicas
input_a = input("Valor A (0 o 1): ")
input_b = input("Valor B (0 o 1): ")
operation = input("Operación: ")

calculate(input_a, input_b, operation)
