"""
fizzbuzz.py
===========

This module defines the `FizzBuzz` class, which implements an extended version
of the traditional FizzBuzz game.

The class allows you to:
- Validate user inputs.
- Compute FizzBuzz values for individual numbers.
- Generate full FizzBuzz sequences as lists or formatted text.

Example:
    >>> fb = FizzBuzz(15)
    >>> fb.compute(3)
    'FizzFizz'
    >>> fb.play_to_text()
    '1\n2\nFizzFizz\n4\nBuzzBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\nFizz\n14\nBuzzFizzBuzz'
"""


class FizzBuzz:
    """Represents the FizzBuzz game logic.

    Attributes:
        limit (int): The upper bound for generating FizzBuzz numbers.
    """

    def __init__(self, limit: int = 100):
        """Initialize a new FizzBuzz instance.

        Args:
            limit (int, optional): The maximum number to play up to.
                Defaults to 100.

        Raises:
            ValueError: If the provided limit is not a positive integer.
        """
        self.limit = limit

    # Getters and Setters
    # Getter for limit
    # ---------------------------------------------------------
    # Property: limit
    # ---------------------------------------------------------
    @property
    def limit(self) -> int:
        """int: Get the current FizzBuzz limit value."""
        return self._limit

    # Setter for limit with validation
    @limit.setter
    def limit(self, value: int):
        """Set the FizzBuzz limit after validating it.

        Args:
            value (int): The new limit value.

        Raises:
            ValueError: If the limit is not a positive integer greater than zero.
        """
        if self.is_valid_number(value):
            self._limit = value

    # ---------------------------------------------------------
    # Validation Method
    # ---------------------------------------------------------
    def is_valid_number(self, number: int) -> bool:
        """Validate that a number is a positive integer greater than zero.

        Args:
            number (int): The number to validate.

        Returns:
            bool: True if the number is valid.

        Raises:
            ValueError: If the number is not a positive integer greater than zero.
        """
        if not isinstance(number, int) or number <= 0:
            raise ValueError("Limit/Number to compute must be a positive integer greater than zero.")
        return True
    
    # ---------------------------------------------------------
    # Core FizzBuzz Logic
    # ---------------------------------------------------------
    def compute(self, number: int) -> str:
        """Compute the FizzBuzz result for a single number.

        The rules are:
        - Add "Fizz" if contains the digit 3.
        - Add "Buzz" if contains the digit 5.
        - Add "Fizz" if divisible by 3.
        - Add "Buzz" if divisible by 5.
        - Concatenate all of them if conditions apply.
        - Return the number itself as a string otherwise.

        Args:
            number (int): The number to compute.

        Returns:
            str: The resulting FizzBuzz string.

        Raises:
            ValueError: If the input number is invalid.
        """
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
        
    # ---------------------------------------------------------
    # Output Methods
    # ---------------------------------------------------------
    def play_to_array(self, max: int = None) -> list[str]:
        """Generate a list of FizzBuzz results up to a given number.

        Args:
            max (int, optional): Custom upper limit. Defaults to self.limit.

        Returns:
            list[str]: List of computed FizzBuzz values.
        """
        if max is None:
            max = self.limit
        return [self.compute(i) for i in range(1, max + 1)]


    def play_to_text(self, max: int = None) -> str:
        """Generate the FizzBuzz sequence as a formatted text string.

        Args:
            max (int, optional): Custom upper limit. Defaults to self.limit.

        Returns:
            str: The full FizzBuzz sequence separated by new lines.
        """
        return "\n".join(self.play_to_array(max))