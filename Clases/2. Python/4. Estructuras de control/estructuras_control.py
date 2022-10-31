"""
Tenemos como flujos de control los for, switch e if

Siempre y cuando se cumpla lo que le pasemos se eejcutará X porcion de codigo
"""

a = 5
b = 6

if(a > b):
    print("El numero " + str(a) + " es mayor que " + str(b))
else:
    print("El numero " + str(b) + " es mayor que " + str(a))

"""
podemos tener <, >=,<=, ==, !=
"""
if(a != b):
    print("los numeros son diferentes")

if(a > b and a != b):
    print("El numero " + str(a) + " es mayor que " +
          str(b) + " y los numeros son diferentes")
else:
    print("El numero " + str(b) + " es mayor que " +
          str(a) + " y los numeros son diferentes")

"""
Para concatener condiciones usamos and o en su defecto or, lo cual es equivalente a java con && y ||
y para multiples condiciones de if usamos el elif (else if)
"""


x = 0
while(x < 10):
    print("Este es el valor x: " + str(x))
    x += 1

"""
Se debe tener cuidado con la identacion en python ya que si el x += 1 estuviera a nivel del while, el bucle sería infinito
"""

par = 1
while (par<10):
    if(par%2==0):
        print("El numero " + str(par) + " es par")
    par += 1

"""
Para detener un bucle for o while usamos la palabra brak, y si queremos saltarnos una iteración usamos el continue
"""

lista = [1,2,3,4,5,6,7,8,9]
for i in lista:
    print("este es el valor del elemento en la posicion i" , i)

print("-------------------------------")
for i in range(0, len(lista)):
    print("El mismo valor recorriedo de otra manera, esta es la posicion " + str(i))
    print("Este es el valor " + str(lista[i]))


#switch (no se usa mucho porque es de python 3.10 en adelante y se usa es un match)
valor = 5

match (valor):
    case 1:
        print("el valor usando match que es un switch en python es 1")
    case 2:
        print("el valor usando match que es un switch en python es 2")
    case 3:
        print("el valor usando match que es un switch en python es 3")
    case 4:
        print("el valor usando match que es un switch en python es 4")
    case 5:
        print("el valor usando match que es un switch en python es 5")


#for con else
lista2=["hola","adios"]
for i in lista2:
    if i == "mensaje":
        print("encontre la palabra mensaje")
        break
else:
    print("no existe la palabra mensaje en la lista2")