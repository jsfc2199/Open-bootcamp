public class Main {
    public static void main(String[] args) {
        Coche coche = new Coche(); //se usa el constructor
        coche.velocidad();
        System.out.println(coche.velocidad);

        Coche coche2 = new Coche(); //se usa el constructor

        System.out.println(coche2.velocidad);
        coche2.setMarca("Mazda");//uso del set
        System.out.println("La marca del coche 2 es ".concat(coche2.getMarca())); //uso del get
    }
}

class Coche {
    int numeroPuertas; //por defecto es pública
    int velocidad;//por defecto es pública

    private String marca; //no se puede acceder a ella sin un método de acceso como getMarca()

    //--------------sobre carga de constructores
    //constructor sin argumentos
    public Coche() {
        System.out.println("estoy en el constructor sin parametros");
    }

    //constructor con argumentos
    public Coche(int numeroPuertas, int velocidad) {
        this.numeroPuertas = numeroPuertas;
        this.velocidad = velocidad;
    }

    //metodo
    public void velocidad() {
        velocidad += 15;
    }

    //------------------------------------------esto es encapsulación
    //para acceder a la marca del carro
    public String getMarca() {
        return marca;
    }

    //para darle valor a la marca del carro
    public void setMarca(String marca) {
        this.marca = marca;
    }
}

//--------------clases y metodos abstractos, y no puede ser instanciada
abstract class vehiculo{
    private String tipo;

    private String sonido;

    int numeroPuertas;
    int velocidad;

    private String marca;


    //metodo
    public void velocidad() {
        velocidad += 15;
    }

    //------------------------------------------esto es encapsulación
    //para acceder a la marca del carro
    public String getMarca() {
        return marca;
    }

    //para darle valor a la marca del carro
    public void setMarca(String marca) {
        this.marca = marca;
    }

    //métodos abstractos sin cuerpo, es decir, al heredar esta clase se debe dar cuerpo a estos métodos
    abstract public void setSonido(String sonido) ;

    abstract public String getSonido() ;


}