"""Es escribir codigo reutilizable, o para reducir la complejidad de mi código.
Deben o deberían realizar una unica tarea
"""

# estructura de una función


def nombre():
    pass


def suma(a, b):
    return a + b


print(suma(2, 2))


#funcion dentro de otra funcion, pero no es muy comun
def matematicas(a, b):
    def resta(a, b):
        print(a - b)

    resta(a, b)

matematicas(5, 3)

hoyhace=12
def otraFuncion():
    global hoyhace
    hoyhace=6
    print("Estamos afectando a la variable global de afuera desde adentro de la funcion")

#parametros opcionales o por defecto, si no le paso nada como valor a la funcion tomará el nombre juan
def porDefecto(nombre = 'Juan'):
    print("hola", nombre)

#funcion con muchos valores, es decir, con 0 o más parámetros
def muchosValores(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

print(muchosValores(1,2,3,4,5,6,7,8,9))

def impirminedoDiccionario(**kwargs):
    for k, v in kwargs.items():
        print(k, "=", v)
    print(kwargs)

impirminedoDiccionario(coche="lindo", juan="franco")

def multipleReturn(a,b):
    return a+b, a-b, a*b, a/b

sumar, restar, multi, div = multipleReturn(2,4) #debo guardar los valos en una unica variable o multiples como este caso
print(sumar)
print(restar)
print(multi)
print(div)

#funciona lambda o anonima
anonima = lambda : print("hola")
anonima()

anonimaConParametros = lambda nombre,nombre2: print("hola", nombre, "adios", nombre2)
anonimaConParametros("juan","pedro")

anonimaConReturn = lambda x: x+x #lo primero son los parametros que recibe y lo siguien es el return
print(anonimaConReturn(2))