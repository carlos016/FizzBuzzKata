"""Refactored FizzBuzz implementation.

Public API preserved for compatibility with existing tests and scripts:
- class FizzBuzz(limit: int = 100)
- property: limit
- method: is_valid_number(number: int) -> bool
- method: compute(number: int) -> str
- method: play_to_array(max: int | None = None) -> list[str]
- method: play_to_text(max: int | None = None) -> str
"""

from __future__ import annotations
from typing import List


class FizzBuzz:
    """FizzBuzz game logic with centralized validation and clearer helpers."""

    def __init__(self, limit: int = 100):
        # use the setter to validate
        self.limit = limit

    @property
    def limit(self) -> int:
        """Configured upper bound for output methods."""
        return self._limit

    @limit.setter
    def limit(self, value: int) -> None:
        self._validate_positive_integer(value, name="limit")
        self._limit = value

    # Validation helpers
    def _validate_positive_integer(self, value, name: str = "number") -> None:
        """Raise ValueError unless ``value`` is an int > 0.

        This method is strict about types because existing tests expect
        ValueError for non-int inputs.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer greater than zero.")

    def is_valid_number(self, number: int) -> bool:
        """Backward-compatible wrapper used by legacy callers/tests.

        Returns True when validation passes, otherwise raises ValueError.
        """
        self._validate_positive_integer(number)
        return True

    # Core logic
    def compute(self, number: int) -> str:
        """Compute the FizzBuzz token for a single integer.

        Rules (preserved): presence-based tokens first (contains digits), then
        divisibility tokens. If no rule applies, return the number as a string.
        """
        self._validate_positive_integer(number, name="Number")

        s = str(number)
        tokens: List[str] = []

        # presence-based tokens
        if '3' in s:
            tokens.append("Fizz")
        if '5' in s:
            tokens.append("Buzz")

        # divisibility-based tokens
        if number % 3 == 0:
            tokens.append("Fizz")
        if number % 5 == 0:
            tokens.append("Buzz")

        return "".join(tokens) if tokens else s

    # Output helpers
    def play_to_array(self, max: int | None = None) -> List[str]:
        if max is None:
            max = self.limit
        self._validate_positive_integer(max, name="max")
        return [self.compute(i) for i in range(1, max + 1)]

    def play_to_text(self, max: int | None = None) -> str:
        return "\n".join(self.play_to_array(max))