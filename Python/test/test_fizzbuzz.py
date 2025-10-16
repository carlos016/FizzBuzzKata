# Importamos el módulo pytest para crear pruebas TDD
import pytest
from src.fizzbuzz import FizzBuzz

# Definimos la clase de test que contendrá los métodos de prueba
class TestFizzBuzz:
    # Definimos el méodo setup que instanciará el objeto FizzBuzz
    def setup_method(self):
        self.max = 100
        self.fizzbuzz = FizzBuzz(self.max)

    # Definimos el método de test que probará la instanciación de la clase FizzBuzz    
    def test_fizzbuzz_instantiation(self):
        assert isinstance(self.fizzbuzz, FizzBuzz)
        assert self.fizzbuzz.limit == self.max
