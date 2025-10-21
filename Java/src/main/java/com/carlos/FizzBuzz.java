package com.carlos;

import java.util.ArrayList;
import java.util.List;

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
    }

    // Validation
    private boolean isValidNumber(int number) {
        if (number <= 0) {
            throw new IllegalArgumentException("The limit/Number must be a positive integer greater than zero.");
        }
        return true;
    }

    public String compute (int number) {
        String result = "";
        if (isValidNumber(number)){
            if (String.valueOf(number).contains("3")){
                result += "Fizz";
            }
            if (String.valueOf(number).contains("5")){
                result += "Buzz";
            }
            if (number % 3 == 0){
                result += "Fizz";
            }
            if (number % 5 == 0){
                result += "Buzz";
            }
        }
        if (result.isEmpty()){
            result = String.valueOf(number);
        }
        return result;
    }

    public List<String> playToList(){
        return playToList(getLimit());
    }

    public List<String> playToList(int max){
        if (isValidNumber(max)){
            List<String> results = new ArrayList<>(max);
            for (int i = 0; i < max; i++){
                results.add(compute(i + 1));
            }
            return results;
        }
        return new ArrayList<>();
    }

    public String playToText(){
        return playToText(getLimit());
    }

    public String playToText(int max){
        List<String> results = playToList(max);
        return String.join("\n", results);
    }
}
