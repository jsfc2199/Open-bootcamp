import java.util.Objects;

public class Main {
    public static void main(String[] args) {
    }
}

//--------------herencia entre Vehiculo y, coche y moto
abstract class Vehiculo {
    int velMax;
    String matricula;
    String sonido;

    public boolean compruebaMatricula(String matricula) {
        return Objects.equals(matricula, "xxx");
    }

    public abstract String getSonido();

    public abstract void setSonido(String sonido);
}

//si ponemos final, no podemos usar esta clase para heredar de ella
final class Coche extends Vehiculo {

    //aplicamos los métodos abstractos
    @Override
    public String getSonido() {
        return "Este es el sonido del coche " + this.sonido;
    }

    @Override
    public void setSonido(String sonido) {
        this.sonido = sonido;
    }
}

class Moto extends Vehiculo {

    //aplicamos los métodos abstractos
    @Override
    public String getSonido() {
        return "Este es el sonido de la moto" + this.sonido;
    }

    @Override
    public void setSonido(String sonido) {
        this.sonido = sonido;
    }
}

/*class CocheElectrico extends Coche {

}*/