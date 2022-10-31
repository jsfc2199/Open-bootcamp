class Alumno:
    _nombre = None
    _nota = None

    def setNombre(self, nombre):
        self._nombre = nombre

    def setNota(self, nota):
        self._nota = nota

    def aprobado(self, nota):
        if(nota>5):
            return "aprobado"
        return "no aprobado"

alumno1 = Alumno()
alumno2 = Alumno()

alumno1.setNombre("Juan")
alumno2.setNombre("Carlos")

alumno1.setNota(5)
alumno2.setNota(6)

print("El alumno", alumno1._nombre, "tiene como nota" , alumno1._nota, "por lo tanto su estado es:", alumno1.aprobado(alumno1._nota))
print("El alumno", alumno2._nombre, "tiene como nota" , alumno2._nota, "por lo tanto su estado es:", alumno2.aprobado(alumno2._nota))