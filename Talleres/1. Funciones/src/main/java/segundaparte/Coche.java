package segundaparte;

public class Coche {
    private int numeroPuertas;

    public Coche(int numeroPuertas) {
        this.numeroPuertas = numeroPuertas;
    }

    public int aumentarPuertas(){
        return this.numeroPuertas++;
    }

    public int NumeroPuertas() {
        return numeroPuertas;
    }
}
