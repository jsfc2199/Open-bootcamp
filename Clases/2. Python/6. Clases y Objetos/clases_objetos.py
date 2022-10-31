"""
Crearemos nuestros primeros objetos para poder aplicar POO

Un objeto es representar los objetos de la vida real en código, los cuales cuentan con atributos (propiedades) y métodos

En python no existe la proteccion de propiedades, no existe, private, public, etc

Cuando queremos indicar que un atributo no es modificable lo hacemos con guion bajo, es decir, _color
Luego para cambiar el valor de forma
"""

# creamos una clase (esto es dinámica), para modificar una propiedad en una clase dinámica usamos el self


class dinosaurio:

    # propiedades
    color = 'verde'
    _encendido = True

    # metodos
    def apagar(self):
        self._encendido = False  # self es como el this en java

    def enciende(self):
        self._encendido = True


# instancia de dinosaurio, es decir un objeto. En java seria dinosario dinosaurio = new dinosaurio()
dinosaurio1 = dinosaurio()

# accedo a las propiedades
print(dinosaurio1.color)  # imprimre verde

dinosaurio1.color = 'white'
print(dinosaurio1.color)  # imprime white

print(dinosaurio1._encendido)
dinosaurio1.apagar()
print(dinosaurio1._encendido)


# clases estaticas, para modificar una propiedad de una clase estática llamamos en la función a la propia clase
class Estatica:
    numero = 1

    def incrementa():
        # numero no es una instancia nueva por cada llamada, siempre es la misma
        Estatica.numero += 1


Estatica.incrementa()
Estatica.incrementa()
Estatica.incrementa()
Estatica.incrementa()
print(Estatica.numero)

# ----------------------Herencia en python
class Vehiculo:
    _encendido = True
    def apagar(self):
        self._encendido = False
    def encender(self):
        self._encendido = True

class Coche(Vehiculo):
    _marca = ""
    def darMarca(self, marca):
        self._marca = marca

coche = Coche()
coche.darMarca("mazda")
print(coche._marca) #este atributo es propio de la clase coche
print(coche._encendido) #tengo acceso a lo que tiene el padre
coche.apagar() #inclcuso a los metodos
print(coche._encendido)

#herencia multiple en python
class Carroceria:
    carroceria = True
    def noTieneCarroceria(self):
        self.carroceria = False

#tengo acceso a lo de vehiculo, carroceria y a lo que escriba dentro de moto
class Moto(Vehiculo, Carroceria):
    pass

#clase con constructor
class Juan():   
    _apellido = None
    _edad = None
    def __init__(self, nombre, apellido, edad): #siempre se llama __init__ y siempre lleva el self, y lo que reciba son los parametros
        print("estoy en el constructor", nombre)
        self._apellido = apellido
        self._edad = edad

juan = Juan("juan","franco",25) #con la instancia paso parametros de construtor
print(juan._apellido)
print(juan._edad)

#si el constructor de la padre tiene parametos y el hijo está heredando, para darle valores hacemos
class Padre():
    def __init__(self, nombre, apellido):
        print("estoy en el constructor del patre")
        print("hola",nombre,apellido)

class Hijo(Padre):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        print("estoy en el hijo")

hijo = Hijo("juan", "frnaco")

"""
Las clases en python, realmente son diccionarios, donde los atributos son las claves, y los valores que les demos son el valor, pero se usan las clases para
mejor sintaxis
"""

#clases abstractas
"""
Para ellas debemos hacer el import from abc import ABC, abstractmethod. Tal como en java, estas no se pueden instanciar
Sirven para definir un conjunto de funciones comunes para otras clases y heredar, se aplica el concepto de polimorfismo
"""

from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("wow")

class Gato(Animal):
    def sonido(self):
        print("miaw")

perro = Perro()
perro.sonido()

gato =Gato()
gato.sonido()

"""
Relacios HAS-A, significa contiene, y es la composición que indica que una clase está compuesta de otra clase

La relación A-HAS es lo mismo que herencia

Ambas se pueden combinar, tener una clase compuesta y usar esta en otra de forma heredada
"""
class Motor:
    tipo = "diesel"    

class Ventanas:
    numero = 4    

#coche se compone de otras clases
class OtroCoche:
    motor = Motor()
    ventanas = Ventanas()
    
otroCoche = OtroCoche()
print(otroCoche.motor.tipo) #hay que ir a diferentes niveles para poder acceder a lo que realmente queremos
print(otroCoche.ventanas.numero) #con esto tenemos jerarquia de clases

