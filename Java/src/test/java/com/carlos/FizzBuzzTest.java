package com.carlos;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

/**
 * Unit test suite for the {@link FizzBuzz} class.
 *
 * <p>These tests follow the TDD approach: tests are written first,
 * and the implementation is added afterwards.</p>
 */
public class FizzBuzzTest {

    /**
     * Shared {@link FizzBuzz} instance created once before all tests.
     * <p>This instance is reused across tests to ensure consistent behavior.</p>
     * <p>It is initialized with a maximum value of {@link #MAX}.</p>
     */
    private static FizzBuzz fizzBuzz;
    private static final int MAX = 100;

    /**
     * Initializes shared state once before all tests in this class.
     * <p>Using {@code @BeforeAll} reduces setup overhead by creating a single
     * instance reused across tests. The setup method must be static.</p>
     */
    @BeforeAll
    public static void setUp() {
        fizzBuzz = new FizzBuzz(MAX);
    }

    /**
     * Verifies that the {@link FizzBuzz} class can be instantiated.
     *
     * <p>This test is the simplest case of the kata: the class should
     * construct without throwing and must not be {@code null}.</p>
     */
    @Test
    public void canInstantiateFizzBuzz() {
        assertNotNull(fizzBuzz, "FizzBuzz instance should not be null");
        assertEquals(MAX, fizzBuzz.getLimit());
    }

    @Test
    public void constructorThrowsOnInvalidLimit() {
        /**
         * Ensures the constructor validates its input and throws
         * {@link IllegalArgumentException} for non-positive integer limits and zero.
         */
        var ex1 = assertThrows(IllegalArgumentException.class, () -> new FizzBuzz(0));
        var ex2 = assertThrows(IllegalArgumentException.class, () -> new FizzBuzz(-5));

        assertTrue(ex1.getMessage().contains("limit"));
        assertTrue(ex2.getMessage().contains("limit"));
    }

    @Test
    public void computeNormalNumbers() {
        /**
         * Verifies compute() returns the number as a string for inputs that not contains 
         * 3 or 5 and are not multiples of 3 or 5.
         */
        assertEquals("1", fizzBuzz.compute(1));
        assertEquals("2", fizzBuzz.compute(2));
        assertEquals("4", fizzBuzz.compute(4));
        assertEquals("7", fizzBuzz.compute(7));
        assertEquals("98", fizzBuzz.compute(98));
    }

    @Test
    public void computeFizzNumbers() {
        /**
         * Verifies compute() returns "Fizz" for numbers that contain
         * 3 or are divisible by 3 but are not divisible by 5 or contain 5 (according to the kata rules implemented).
         */
        assertEquals("Fizz", fizzBuzz.compute(6));
        assertEquals("Fizz", fizzBuzz.compute(9));
        assertEquals("Fizz", fizzBuzz.compute(27));
        assertEquals("Fizz", fizzBuzz.compute(42));
    }

    @Test
    public void computeBuzzNumbers() {
        /**
         * Verifies compute() returns "Buzz" for numbers that contain
         * 5 or are divisible by 5 but are not divisible by 3 or contain 3 (according to the kata rules implemented).
         */
        assertEquals("Buzz", fizzBuzz.compute(10));
        assertEquals("Buzz", fizzBuzz.compute(20));
        assertEquals("Buzz", fizzBuzz.compute(40));
        assertEquals("Buzz", fizzBuzz.compute(100));
    }

    @Test
    public void computeAnyFizzBuzzNumbers() {
        /**
         * Verifies compute() behavior for composite cases where both "Fizz"
         * and "Buzz" might appear according to the kata's specific rules.
         */
        assertEquals("FizzFizz", fizzBuzz.compute(3));
        assertEquals("BuzzBuzz", fizzBuzz.compute(5));
        assertEquals("BuzzFizzBuzz", fizzBuzz.compute(15));
        assertEquals("FizzFizzBuzz", fizzBuzz.compute(30));
        assertEquals("FizzBuzzBuzz", fizzBuzz.compute(35));
        assertEquals("BuzzFizzBuzz", fizzBuzz.compute(45));
        assertEquals("FizzBuzz", fizzBuzz.compute(53));
        assertEquals("BuzzFizzBuzz", fizzBuzz.compute(75));
        assertEquals("FizzBuzz", fizzBuzz.compute(90));
    }

    @Test
    public void computeThrowsOnInvalidNumber() {
        /**
         * Ensures compute() validates its input and throws
         * {@link IllegalArgumentException} for non-positive integer limits and zero.
         */
        var ex1 = assertThrows(IllegalArgumentException.class, () -> fizzBuzz.compute(0));
        var ex2 = assertThrows(IllegalArgumentException.class, () -> fizzBuzz.compute(-10));

        assertTrue(ex1.getMessage().contains("Number"));
        assertTrue(ex2.getMessage().contains("Number"));
    }

    @Test
    public void playFizzBuzzUpToLimitToList() {
        /**
         * Verifies playToList() returns the full FizzBuzz sequence up to the
         * configured limit and that its elements match the expected sequence
         * computed by calling {@link #compute(int)} repeatedly.
         */
        List<String> expected = new ArrayList<>();
        for (int i = 0; i < MAX; i++) {
            expected.add(fizzBuzz.compute(i + 1));
        }

        List<String> actual = new ArrayList<>(fizzBuzz.playToList());

        assertEquals(expected.size(), actual.size(), "Array lengths should match");
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i), actual.get(i), "Mismatch at index " + i);
        }
    }

    @Test
    public void playFizzBuzzUpToLimitToText() {
        /**
         * Verifies playToText() returns a newline-separated representation of the
         * full FizzBuzz sequence equivalent to joining the list returned by
         * {@link #playFizzBuzzUpToLimitToList()}.
         */
        List<String> expectedList = fizzBuzz.playToList();
        String expected = String.join("\n", expectedList);

        String actual = fizzBuzz.playToText();

        assertEquals(expected.length(), actual.length(), "Text lengths should match");
        assertEquals(expected, actual, "Mismatch in expected and actual text output");
    }
}
