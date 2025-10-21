package com.carlos;

/**
 * Simple implementation of the classic FizzBuzz kata.
 *
 * <p>This class holds a configurable <em>limit</em> that can be used by
 * methods that produce the FizzBuzz sequence. The limit must be a
 * positive integer; invalid values fall back to a default.</p>
 */
public class FizzBuzz {

    /** Current upper bound used by FizzBuzz operations. */
    private int limit;

    /** Default maximum limit used when an invalid value is provided. */
    private static final int MAX = 100;

    // Constructors
    /**
     * Creates a {@code FizzBuzz} instance with the default limit ({@value #MAX}).
     */
    public FizzBuzz() {
        this(MAX);
    }

    /**
     * Creates a {@code FizzBuzz} instance with the given limit.
     *
     * @param max the upper bound to use; if {@code max} is not positive the default
     *            value {@value #MAX} will be used instead
     */
    public FizzBuzz(int max) {
        setLimit(max);
    }

    // Getters and Setters
    /**
     * Returns the configured limit for this {@code FizzBuzz} instance.
     *
     * @return the limit (always positive)
     */
    public int getLimit() {
        return limit;
    }

    /**
     * Sets the limit for this instance. The method is {@code final} to avoid
     * accidental overriding and to keep construction safe.
     *
     * @param max the new limit; if it is not positive the default {@value #MAX}
     *            will be applied
     */
    public final void setLimit(int max) {
        if (isValidNumber(max)) {
            this.limit = max;
        }
        else {
            this.limit = MAX;
        }
    }

    // Validation
    /**
     * Returns {@code true} when the provided number is valid as a limit.
     *
     * @param number the number to validate
     * @return {@code true} if the number is greater than zero
     */
    private boolean isValidNumber(int number) {
        return number > 0;
    }
    
}
