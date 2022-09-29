package ejercicioWhile;

public class Main {
    public static void main(String[] args) {
        int numeroWhile = -5;
        bucleWhile(numeroWhile);
    }

    public static int bucleWhile(int numeroWhile){
        while (numeroWhile < 3){
            System.out.println(numeroWhile);
            numeroWhile++;
        }
        return numeroWhile;
    }
}
