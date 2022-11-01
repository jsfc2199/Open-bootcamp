#r read, a append, w escritura, x create, t texto, b binary, letra+. Lo stipos cos son r y w+
f = open('C:/Users/RYZEN/Desktop/juegostxt.txt', 'r')

datos = f.read()
print(datos)
print("-------------------")

"""
datos2 = f.readlines() #guardarlo como lista

print(datos2)

for linea in datos2:
    if linea[0] == '#':
        conntinue
    print(linea)
"""

f.close()