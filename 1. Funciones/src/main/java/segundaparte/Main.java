package segundaparte;

public class Main {
    public static void main(String[] args) {
        Coche miCoche = new Coche(4);
        miCoche.aumentarPuertas();

        System.out.println(miCoche.NumeroPuertas());
    }
}
