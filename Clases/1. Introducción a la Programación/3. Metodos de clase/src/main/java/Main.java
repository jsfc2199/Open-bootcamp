import interfaces.OperacionesI;

public class Main {
    public static void main(String[] args) {
        OperacionesI operacionesI = new OperacionesI();
        System.out.println(operacionesI.sumar(5, 8)); //usando la interfaz

        System.out.println(potencia(10, 5)); //usando métodos estáticos

        System.out.println(factorial(5));

    }

    public static double potencia(int base, int exponente){
        return Math.pow(base,exponente);
    }

    //ejemplo recursividad
    public static int factorial(int numero){
        int resultado;
        if(numero==1){
            return 1;
        }
        resultado = factorial(numero-1)*numero;
        return resultado;
    }

    //recursividad infinita
    public static int suma(int a, int b){
        var temp = a + b;
        return suma(a, temp);
    }

    //recursividad finita
    public static void suma2(int a, int b){
        var temp = a + b;
        if(b>=90){
            return;
        }
        suma(a, temp);
    }
}