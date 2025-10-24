"""
test_fizzbuzz.py
================

TDD tests for the FizzBuzz class using pytest.
These tests validate both the normal behavior and error handling
for the main methods of the FizzBuzz class.
"""

# Import the pytest module to create TDD tests
import pytest
# Import the FizzBuzz class from the fizzbuzz module
from src.fizzbuzz import FizzBuzz


class TestFizzBuzz:
    """Test suite for the FizzBuzz class."""

    def setup_method(self):
        """Create a FizzBuzz instance before each test."""
        self.max = 100
        self.fizzbuzz = FizzBuzz(self.max)

    def test_fizzbuzz_instantiation(self):
        """Verify that a FizzBuzz object is correctly instantiated."""
        assert isinstance(self.fizzbuzz, FizzBuzz)
        assert self.fizzbuzz.limit == self.max

    def test_fizzbuzz_invalid_limit(self):
        """Ensure ValueError is raised for invalid limits."""
        with pytest.raises(ValueError):
            FizzBuzz(-1)
        with pytest.raises(ValueError):
            FizzBuzz(0)
        with pytest.raises(ValueError):
            FizzBuzz("a")   

    def test_fizzbuzz_compute(self):
        """Test the compute() method for expected FizzBuzz outputs."""
        assert self.fizzbuzz.compute(1) == "1"
        assert self.fizzbuzz.compute(2) == "2"
        assert self.fizzbuzz.compute(3) == "FizzFizz"
        assert self.fizzbuzz.compute(5) == "BuzzBuzz"
        assert self.fizzbuzz.compute(9) == "Fizz"
        assert self.fizzbuzz.compute(10) == "Buzz"
        assert self.fizzbuzz.compute(15) == "BuzzFizzBuzz"
        assert self.fizzbuzz.compute(30) == "FizzFizzBuzz"
        assert self.fizzbuzz.compute(35) == "FizzBuzzBuzz"
        assert self.fizzbuzz.compute(53) == "FizzBuzz"

    def test_fizzbuzz_invalid_compute(self):
        """Ensure compute() raises ValueError for invalid inputs."""
        with pytest.raises(ValueError):
            self.fizzbuzz.compute(0)
        with pytest.raises(ValueError):
            self.fizzbuzz.compute(-5)
        with pytest.raises(ValueError):
            self.fizzbuzz.compute("a")

    def test_fizzbuzz_play_to_array(self):
        """Check that play_to_array() returns the correct sequence."""
        assert self.fizzbuzz.play_to_array() == [self.fizzbuzz.compute(i) for i in range(1, self.max + 1)]
        assert self.fizzbuzz.play_to_array(50) == [self.fizzbuzz.compute(i) for i in range(1, 51)]

    def test_fizzbuzz_play_to_text(self):
        """Check that play_to_text() returns the correct formatted string."""
        assert self.fizzbuzz.play_to_text() == "\n".join(self.fizzbuzz.play_to_array())
        assert self.fizzbuzz.play_to_text(50) == "\n".join(self.fizzbuzz.play_to_array(50))