
import math

kilogramos = int(input("Ingresa tu peso en kilogramos: "))

estatura = float(input("Ingresa tu estatura en metros: "))

imc = round(kilogramos/math.pow(estatura, 2), 2)

print("Tu  índice de masa corporal es " + str(imc))