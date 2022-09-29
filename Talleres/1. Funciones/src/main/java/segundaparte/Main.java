package segundaparte;

public class Main {
    public static void main(String[] args) {
        Coche miCoche = new Coche(4);
        System.out.println("El coche inició con " + miCoche.NumeroPuertas());
        miCoche.aumentarPuertas();

        System.out.println("El coche al aumentar las puertas tiene " + miCoche.NumeroPuertas() + " puertas");
    }
}
