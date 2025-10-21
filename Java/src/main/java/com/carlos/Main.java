package com.carlos;

/**
 * Small CLI entrypoint for the FizzBuzz application.
 *
 * <p>This {@code Main} class reads an optional integer limit from standard input
 * and prints the FizzBuzz output up to that limit. If the input is empty or invalid,
 * a sensible default is used.</p>
 */
public class Main {

    /**
     * Application entry point.
     *
     * <p>Reads a single line from standard input. If the user provides a positive
     * integer greater than zero it will be used as the upper bound for the FizzBuzz sequence;
     * otherwise a default value is used. The resulting FizzBuzz text is printed to stdout.</p>
     *
     * @param args command line arguments (ignored)
     */
    public static void main(String[] args) {
        // default limit
        int max = 100;
        try (java.util.Scanner scanner = new java.util.Scanner(System.in)) {
            System.out.print("Ingrese el límite (o presione Enter para usar " + max + "): ");
            String input = scanner.nextLine();
            if (!input.isEmpty()) {
                try {
                    max = Integer.parseInt(input);
                } catch (NumberFormatException e) {
                    System.out.println("Entrada no válida. Usando el límite predeterminado de " + max + ".");
                }
            }
        } catch (Exception e) {
            System.out.println("Error al leer la entrada. Usando el límite predeterminado de " + max + ".");
        }

        FizzBuzz fizzBuzz = new FizzBuzz(max);
        String result = fizzBuzz.playToText();
        System.out.println(result);
    }
}
