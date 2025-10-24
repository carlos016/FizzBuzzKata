"""
test_fizzbuzz.py
================

TDD tests for the FizzBuzz class using pytest.
These tests validate both the normal behavior and error handling
for the main methods of the FizzBuzz class.
"""

import pytest

from src.fizzbuzz import FizzBuzz


@pytest.fixture
def fizzbuzz():
    return FizzBuzz(100)


def test_fizzbuzz_instantiation(fizzbuzz):
    assert isinstance(fizzbuzz, FizzBuzz)
    assert fizzbuzz.limit == 100


@pytest.mark.parametrize("bad", [-1, 0, "a"])
def test_fizzbuzz_invalid_limit(bad):
    with pytest.raises(ValueError):
        FizzBuzz(bad)


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "1"),
        (2, "2"),
        (3, "FizzFizz"),
        (5, "BuzzBuzz"),
        (9, "Fizz"),
        (10, "Buzz"),
        (15, "BuzzFizzBuzz"),
        (30, "FizzFizzBuzz"),
        (35, "FizzBuzzBuzz"),
        (53, "FizzBuzz"),
    ],
)
def test_fizzbuzz_compute(n, expected, fizzbuzz):
    assert fizzbuzz.compute(n) == expected


@pytest.mark.parametrize("bad", [0, -5, "a"])
def test_fizzbuzz_invalid_compute(bad, fizzbuzz):
    with pytest.raises(ValueError):
        fizzbuzz.compute(bad)


def test_fizzbuzz_play_to_array_and_text(fizzbuzz):
    assert fizzbuzz.play_to_array() == [fizzbuzz.compute(i) for i in range(1, fizzbuzz.limit + 1)]
    assert fizzbuzz.play_to_array(50) == [fizzbuzz.compute(i) for i in range(1, 51)]
    assert fizzbuzz.play_to_text() == "\n".join(fizzbuzz.play_to_array())
    assert fizzbuzz.play_to_text(50) == "\n".join(fizzbuzz.play_to_array(50))