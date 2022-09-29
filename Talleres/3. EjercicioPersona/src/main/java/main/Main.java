package main;

import persona.Persona;

public class Main {
    public static void main(String[] args) {
        Persona juan = new Persona("Juan", 25, "123456789");

        Persona personaDefault = new Persona();
        personaDefault.setNombre("default");
        personaDefault.setEdad(-5);
        personaDefault.setTelefono("987654321");


        if(personaDefault.verificarEdad(personaDefault.getEdad())){
            System.out.println("Datos persona default");
            System.out.println(personaDefault.getNombre());
            System.out.println("Error al ingresar la edad");
            System.out.println(personaDefault.getTelefono());
        }else{
            System.out.println("Datos persona default");
            System.out.println(personaDefault.getNombre());
            System.out.println(personaDefault.getEdad());
            System.out.println(personaDefault.getTelefono());
        }


        System.out.println("-----------------------------------------");
        System.out.println("Datos juan");
        System.out.println(juan.getNombre());
        System.out.println(juan.getEdad());
        System.out.println(juan.getTelefono());


    }
}
