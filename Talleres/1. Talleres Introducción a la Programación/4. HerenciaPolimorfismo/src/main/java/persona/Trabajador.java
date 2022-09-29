package persona;

public class Trabajador extends Persona{
    private int Salario;

    public Trabajador() {
    }

    public Trabajador(String nombre, int edad, String telefono, int salario) {
        super(nombre, edad, telefono);
        Salario = salario;
    }

    public int getSalario() {
        return Salario;
    }

    public void setSalario(int salario) {
        Salario = salario;
    }
}
