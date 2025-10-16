# Importamos el módulo pytest para crear pruebas TDD
import pytest
# Importamos la clase FizzBuzz desde el módulo fizzbuzz
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

    # Definimos el método de test que comprobará el control de errores
    def test_fizzbuzz_invalid_limit(self):
        with pytest.raises(ValueError):
            FizzBuzz(-1)
        with pytest.raises(ValueError):
            FizzBuzz(0)
        with pytest.raises(ValueError):
            FizzBuzz("a")   

    # Definimos el método de test que probará la funcionalidad compute
    def test_fizzbuzz_compute(self):
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

    # Definimos el método de test que comprobará el control de errores en compute
    def test_fizzbuzz_invalid_compute(self):
        with pytest.raises(ValueError):
            self.fizzbuzz.compute(0)
        with pytest.raises(ValueError):
            self.fizzbuzz.compute(-5)
        with pytest.raises(ValueError):
            self.fizzbuzz.compute("a")

    # Definimos el método de test que probará la funcionalidad play_to_array
    def test_fizzbuzz_play_to_array(self):
        assert self.fizzbuzz.play_to_array() == [self.fizzbuzz.compute(i) for i in range(1, self.max + 1)]
        assert self.fizzbuzz.play_to_array(50) == [self.fizzbuzz.compute(i) for i in range(1, 51)]

    # Definimos el método de test que probará la funcionalidad play_to_text