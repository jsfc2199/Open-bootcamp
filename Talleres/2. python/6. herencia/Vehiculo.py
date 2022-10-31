class Vehiculo:
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def setColor(self,color):
        self.color = color

    def setRuedas(self,ruedas):
        self.ruedas = ruedas

    def setPuertas(self,puertas):
        self.puertas = puertas

