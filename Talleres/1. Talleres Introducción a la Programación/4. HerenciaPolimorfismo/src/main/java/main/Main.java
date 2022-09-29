package main;

import persona.Cliente;
import persona.Persona;
import persona.Trabajador;

public class Main {
    public static void main(String[] args) {

        Cliente carlos = new Cliente("Carlos", 30, "654987321", 15000);

        Cliente cliente2 = new Cliente();
        cliente2.setNombre("Cliente 2");
        cliente2.setEdad(30);
        cliente2.setTelefono("132654987132");
        cliente2.setCredito(6000);

        Trabajador pedro = new Trabajador("Pedro", 50, "876589453",2000);

        Trabajador trabajador2 = new Trabajador();
        trabajador2.setNombre("trabajador 2");
        trabajador2.setEdad(32);
        trabajador2.setTelefono("654987321654");
        trabajador2.setSalario(4500);

        System.out.println("----------carlos-------------");
        System.out.println(carlos.getNombre());
        System.out.println(carlos.getTelefono());
        System.out.println(carlos.getEdad());
        System.out.println(carlos.getCredito());

        System.out.println("----------cliente2-------------");
        System.out.println(cliente2.getNombre());
        System.out.println(cliente2.getTelefono());
        System.out.println(cliente2.getEdad());
        System.out.println(cliente2.getCredito());

        System.out.println("----------pedro-------------");
        System.out.println(pedro.getNombre());
        System.out.println(pedro.getTelefono());
        System.out.println(pedro.getEdad());
        System.out.println(pedro.getSalario());

        System.out.println("----------trabajador2-------------");
        System.out.println(trabajador2.getNombre());
        System.out.println(trabajador2.getTelefono());
        System.out.println(trabajador2.getEdad());
        System.out.println(trabajador2.getSalario());

    }
}
