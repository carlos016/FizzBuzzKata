# Importa la clase FizzBuzz desde el módulo src.fizzbuzz
from src.fizzbuzz import FizzBuzz

# Función principal que ejecuta el juego FizzBuzz
def main():
    fizzbuzz = FizzBuzz()
    numeroDeseado = 100
    # Obten el numero del usuario
    try:
        numeroDeseado = int(input(f"Introduce un número entero positivo mayor que cero (por defecto {fizzbuzz.limit}): ") or fizzbuzz.limit)
        fizzbuzz.limit = numeroDeseado
    except ValueError as e:
        print(f"Error: {e}. Usando el valor por defecto {fizzbuzz.limit}.")

    print(fizzbuzz.play_to_text())

# Ejecuta la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()