# Importamos el módulo pytest para crear pruebas TDD
import pytest
from fizzbuzz import FizzBuzz

# Definimos la clase de test que hereda de unittest.TestCase
class TestFizzBuzz:
    # Definimos el méodo setup que instanciará el objeto FizzBuzz
    def setup_method(self):
        self.fizzbuzz = FizzBuzz(100)

    # Definimos el método de test que probará la instanciación de la clase FizzBuzz    
    def test_fizzbuzz_instantiation(self):
        assert self.fizzbuzz.limit == 100