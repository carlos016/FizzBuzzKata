# FizzBuzz implementation in Python
class FizzBuzz:
    def __init__(self, limit=100):
        self.limit = limit

    # Getters and Setters
    # Getter para limit
    @property
    def limit(self):
        return self._limit
    # Setter para limit con validación
    @limit.setter
    def limit(self, value):
        if self.is_valid_number(value):
            self._limit = value

    # Método para validar el límite
    def is_valid_number(self, number):
        if not isinstance(number, int) or number <= 0:
            raise ValueError("Limit/Number to compute must be a positive integer greater than zero.")
        return True
    
    # Método para calcular el valor FizzBuzz de un número
    def compute(self, number):
        # Validamos el número, solo lo hacemos si es válido
        if self.is_valid_number(number):
            result = ""
            # Si el número contiene 3 o 5, añadimos Fizz o Buzz respectivamente
            if '3' in str(number):
                result += "Fizz"
            if '5' in str(number):
                result += "Buzz"
            # Si el número es múltiplo de 3 o 5, añadimos Fizz o Buzz respectivamente
            if number % 3 == 0:
                result += "Fizz"
            if number % 5 == 0:
                result += "Buzz"
            # Si no se ha añadido nada, devolvemos el número como cadena
            return result if result else str(number)
    
