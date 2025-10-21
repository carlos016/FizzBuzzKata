package com.carlos;

public class FizzBuzz {

    private int limit;
    private static final int MAX = 100;

     // Constructors

    public FizzBuzz() {
        this(MAX);
    }

    public FizzBuzz(int max) {
        setLimit(max);
    }

    // Getters and Setters
    public int getLimit() {
        return limit;
    }

    public final void setLimit(int max) {
        if (isValidNumber(max)) {
            this.limit = max;
        }
        else {
            this.limit = MAX;
        }
    }

    // Validation
    private boolean isValidNumber(int number) {
        return number > 0;
    }
    
}
