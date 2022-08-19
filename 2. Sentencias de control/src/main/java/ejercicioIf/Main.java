package ejercicioIf;

public class Main {
    public static void main(String[] args) {
        int numeroIf = 5;
        System.out.println(positivoNegativo(numeroIf));

        int numeroIf2 = 0;
        System.out.println(positivoNegativo(numeroIf2));

        int numeroIf3 = -5;
        System.out.println(positivoNegativo(numeroIf3));
    }

    public static String positivoNegativo(int numeroIf) {
        if (numeroIf < 0) {
            return "El numero es negativo";
        } else if (numeroIf == 0) {
            return "El numero es igual a 0";
        }
        return "El numero es positivo";
    }
}
