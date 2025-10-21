package com.carlos;

public class Main {
    public static void main(String[] args) {
        // Obtener el límite del usuario por teclado o usar el valor predeterminado
        int max = 100; // Valor predeterminado
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
        }
        catch (Exception e) {
            System.out.println("Error al leer la entrada. Usando el límite predeterminado de " + max + ".");
        }
        FizzBuzz fizzBuzz = new FizzBuzz(max);
        String result = fizzBuzz.playToText();
        System.out.println(result);
    }
}
