class Vehiculo:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

vehiculo = Vehiculo("rojo","mazda")

fichero = open('guardarVehiculo.txt', 'w')
fichero.write(vehiculo.color)
fichero.write('\n')
fichero.write(vehiculo.marca)

fichero.close()
