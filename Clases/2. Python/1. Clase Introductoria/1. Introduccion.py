
"""
Interprete para enviar comandos.

Esto es un lenguaje interpretado, es decir, no se ejecuta directamente en el procesador si no en un interprete
como spyder.

Un interpretado es más lento que un compilado, pero es más fácil de depurar y tiene ciertas más ventajas.
Un lenguaje compilado se ejecuta directamente en el procesador de la máquina.

Python tiene su propio interprete que es python a su vez ejecutando en cmd python3.

No es necesario indicar los tipos, lo determina atuomáticamente, por lo que es fuertemente dinamico, a diferencia 
de java que es estatico, por lo que hay que indicar el tipo de las variables.

Python al igual que java es fuertemente tipado, es decir, enteros solo se pueden trabajar con enteros
minetras que JS es tipado debil, por ejemplo puedo operar un string y un entero

Es lenguaje orientado a objetos, sin embargo, su principal fuerte es la programación secuencial o declarativa,
junto con la ciencia de datos y el machine learning. Es decir, no nos obliga a tener clases, ni objetos.

Python es usado en gran cantidad de cosas como automatizar tareas, gestionar, o por ejemplo 2 de los mas grandes
proyectos realizados son ansible (ansible.com) y saltStack, ambos son para automatizar tareas y más

Podemos usar python para darle soporte al backend con las librearias Django (la mas usada) y la compentencia es
Flask, que es similar a Django para darle soporte al back.

Para bases de datos una opción psycog o PyGreSQL, otro es mysql connector python, y otro puede ser 
MariaDb python connector que es oritando a servidor, pymongo orientado a bases de datos de mongo, sqLite3 es otra
donde de las anteriores mongo es la unica que es una base de datos no relacional

Ejemplos de librearías sobre data science son numpy y scipy, y pandas (para analisis de datos en tablas)
"""

#esti es declarativo, "vomitamos" código
print("Hola") #los comentarios se inician con el numeral y esto es como se imprimen los valores
x=4 #x y y son variables
y=4
print("La suma es " + str(x+y))


#para orientarlo a clases
class miClase:
    def suma(self, a,b):
        return a+b
    
miClase = miClase() #datos es una instancia de miClase
print(miClase.suma(5, 5))