package ejercicioDoWhile;

public class Main {
    public static void main(String[] args) {
        System.out.println("multiple ejecicion");
        int numeroWhile = 1;
        bucleDoWhile(numeroWhile);

        System.out.println("Unica ejecucion");
        int numeroWhile2 = 3;
        bucleDoWhile(numeroWhile2);
    }

    public static int bucleDoWhile(int numeroWhile) {

        do {
            System.out.println(numeroWhile);
            numeroWhile++;

        } while (numeroWhile < 3);

        return numeroWhile;
    }
}
