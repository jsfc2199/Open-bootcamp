package ejercicioSwitch;

public class Main {
    public static void main(String[] args) {

        String estacion = "Invierno";
        System.out.println(switchEstaciones(estacion));
    }

    public static String switchEstaciones(String estacion){
        return switch (estacion.toLowerCase()) {
            case "invierno" -> "La estacion es invierno";
            case "verano" -> "La estacion es verano";
            case "otoño" -> "La estacion es otoño";
            case "primavera" -> "La estacion es primavera";
            default -> "No corresponde a ninguna estacion";
        };

        //Otra forma para realizar el return del witch usando varios return que igualmente rompen en el flujo y por ende no es necesario usar break
        /*
        switch (estacion.toLowerCase()){
            case "invierno":
                return "La estacion es invierno";
            case "verano":
                return "La estacion es verano";
            case "otoño":
                return "La estacion es otoño";
            case "primavera":
                return "La estacion es primavera";
            default:
                return "No corresponde a ninguna estacion";
        }
        */
    }
}
