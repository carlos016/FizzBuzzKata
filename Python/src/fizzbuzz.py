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
    
