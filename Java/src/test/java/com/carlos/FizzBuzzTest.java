package com.carlos;

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
        assertEquals(fizzBuzz.getLimit(), MAX);
    }

    @Test
    public void constructorThrowsOnInvalidLimit() {
        // Expect IllegalArgumentException when constructing with an invalid limit (e.g. 0 or -1)
        var ex1 = assertThrows(IllegalArgumentException.class, () -> new FizzBuzz(0));
        var ex2 = assertThrows(IllegalArgumentException.class, () -> new FizzBuzz(-5));

        assertTrue(ex1.getMessage().contains("limit"));
        assertTrue(ex2.getMessage().contains("limit"));
    }
}
