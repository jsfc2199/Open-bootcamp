import operaciones
#importamos el modulo operaciones
"""
podemos escribir tambien 
import operaciones as alias
"""

def main():
    res = operaciones.suma(2,2)
    resta= operaciones.resta(2,2)
    print("Hola en main")
    print(res)
    print(resta)
    print(operaciones.nombreModulo())

    op = operaciones.Operador().multi(5,2)
    print(op)

if __name__ == '__main__':
    main()