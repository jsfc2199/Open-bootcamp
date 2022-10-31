def bisciesto(anio):
    if (anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0):
        return "Es bisciensto"
    elif (anio % 4 == 0 and not anio % 100 == 0 and not anio % 400 == 0):
        return "Es bisciesto"
    elif (not anio % 4 == 0 and not anio % 100 == 0 and not anio % 400 == 0):
        return "No Es bisciesto"
    elif (anio % 4 == 0 and anio % 100 == 0 and not anio % 400 == 0):
        return "No Es bisciesto"


print(bisciesto(2019))
print(bisciesto(1981))
print(bisciesto(2020))
print(bisciesto(2012))
print(bisciesto(1900))
print(bisciesto(2100))
print(bisciesto(2000))
print(bisciesto(2400))
