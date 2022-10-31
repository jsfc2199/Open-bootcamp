from Vehiculo import Vehiculo

class Coche(Vehiculo):
    velocidad = None
    cilindrara = None
    color = None
    ruedas = None
    puertas = None


    def __init__(self,velocidad, cilindrara, color, ruedas, puertas):
           super().__init__(color, ruedas, puertas) 
           self.velocidad = velocidad
           self.cilindrara = cilindrara



coche = Coche(200, True, "verde", 4, 4)


print("El color del coche es" , coche.color)
print("La cantidad de ruedas del coche es" , coche.ruedas)
print("La cantidad de puertas del coche es" ,coche.puertas)
print("La velocidad maxima del coche es" ,coche.velocidad)
print("Cuenta con cilindraje" ,coche.cilindrara)


 
