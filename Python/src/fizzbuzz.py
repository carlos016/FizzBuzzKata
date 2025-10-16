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
        if self.is_valid_limit(value):
            self._limit = value

    # Método para validar el límite
    def is_valid_limit(self, limit):
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("Limit must be a positive integer greater than zero.")
        return True
    
