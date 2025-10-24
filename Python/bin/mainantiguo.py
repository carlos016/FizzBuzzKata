"""
main.py
=======

Command-line interface for running the FizzBuzz game.

This script allows the user to run the FizzBuzz game interactively,
setting a custom limit and displaying the results in the terminal.

Example:
    ...\FizzBuzzKata\Python$ python -m bin.main
"""

# Import the FizzBuzz class from the src.fizzbuzz module
from src.fizzbuzz import FizzBuzz


def main():
    """Run the FizzBuzz game interactively from the command line.

    Prompts the user to enter a number (default: current limit) and prints
    the full FizzBuzz sequence up to that number.
    """
    fizzbuzz = FizzBuzz()
    numeroDeseado = 100
    # Get the user's number
    try:
        numeroDeseado = int(input(f"Enter a positive integer greater than zero (default {fizzbuzz.limit}): ") or fizzbuzz.limit)
        fizzbuzz.limit = numeroDeseado
    except ValueError as e:
        print(f"Error: {e}. Using default value {fizzbuzz.limit}.")

    print(fizzbuzz.play_to_text())

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()