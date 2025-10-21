package com.carlos;

import java.util.ArrayList;
import java.util.List;

/**
 * Simple implementation of the classic FizzBuzz kata.
 *
 * <p>This class holds a configurable <em>limit</em> that is used by the
 * provided helper methods to generate the FizzBuzz sequence. The limit
 * and input numbers must be positive integers greater than zero; invalid values 
 * cause an {@link IllegalArgumentException} to be thrown.</p>
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
     * @param max the upper bound to use; must be a positive integer greater than zero
     * @throws IllegalArgumentException if {@code max} is not positive
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
     * @param max the new limit; must be a positive integer greater than zero
     * @throws IllegalArgumentException if {@code max} is not positive
     */
    public final void setLimit(int max) {
        if (isValidNumber(max)) {
            this.limit = max;
        }
    }

    // Validation
    /**
     * Validates a numeric argument used as a limit or input number.
     *
     * @param number the number to validate
     * @return {@code true} when the number is greater than zero
     * @throws IllegalArgumentException when the number is not positive
     */
    private boolean isValidNumber(int number) {
        if (number <= 0) {
            throw new IllegalArgumentException("The limit/Number must be a positive integer greater than zero.");
        }
        return true;
    }

    public String compute (int number) {
        /**
         * Computes the FizzBuzz representation for a single number according
         * to the kata's rules implemented here.
         *
         * <ul>
         *   <li>If the decimal representation contains the digit '3' the
         *       token {@code "Fizz"} is appended.</li>
         *   <li>If the decimal representation contains the digit '5' the
         *       token {@code "Buzz"} is appended.</li>
         *   <li>If the number is divisible by 3 the token {@code "Fizz"}
         *       is appended.</li>
         *   <li>If the number is divisible by 5 the token {@code "Buzz"}
         *       is appended.</li>
         * </ul>
         *
         * The tokens are appended in the order above; if no token was
         * appended the decimal string of the number is returned.
         *
         * @param number the input number to evaluate (must be positive and greater than zero)
         * @return the Fizz/Buzz representation or the decimal number as string
         * @throws IllegalArgumentException if {@code number} is not positive or is not greater than zero
         */
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

    public List<String> playToList(int max){
        /**
         * Produces the full FizzBuzz sequence as a {@link List} of strings
         * up to the provided {@code max} (inclusive of index {@code 1..max}).
         *
         * @param max the upper bound (must be positive)
         * @return a list containing the FizzBuzz representation for each
         *         number from {@code 1} to {@code max}
         * @throws IllegalArgumentException if {@code max} is not positive
         */
        if (isValidNumber(max)){
            List<String> results = new ArrayList<>(max);
            for (int i = 0; i < max; i++){
                results.add(compute(i + 1));
            }
            return results;
        }
        return new ArrayList<>();
    }

    public List<String> playToList(){
        return playToList(getLimit());
    }

    public String playToText(int max){
        /**
         * Produces the full FizzBuzz sequence as a newline-separated text
         * block for numbers {@code 1..max}.
         *
         * @param max the upper bound (must be positive and greater than zero)
         * @return a {@link String} where each line represents the FizzBuzz
         *         value for the corresponding number
         * @throws IllegalArgumentException if {@code max} is not positive
         */
        List<String> results = playToList(max);
        return String.join("\n", results);
    }

    public String playToText(){
        return playToText(getLimit());
    }
}
