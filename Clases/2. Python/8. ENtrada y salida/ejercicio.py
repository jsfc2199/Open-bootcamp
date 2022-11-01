#forma antigua para cadenas
numero = 5
texto = "quijote"
otro = 1.2

print("el numero es %d y el texto es %s , tiene %.2f" %(numero, texto, otro))


#forma con funcion formato 
print("el numero es {} y el texto es {} , tiene {}".format(numero, texto, otro)) #podemos poner las variables en cualquier orden

print("el numero es {2} y el texto es {0} , tiene {1}".format(numero, texto, otro)) #colocando numeros en las llaves cambiamos el orden

print("el numero es {n1} y el texto es {n2} , tiene {n3}".format(n1=numero, n2=texto, n3=otro)) 

#forma avanzada y más flexible
print(f'el numero es {numero} y el texto es {texto.upper()}') #concatenando como javascript

