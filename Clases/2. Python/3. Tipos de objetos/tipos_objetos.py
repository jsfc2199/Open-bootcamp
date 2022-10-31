"""
Tenemos objetos mutables e inmutables, y tiene un recolector de basura donde elimina las variables que dejan de utilizarse, pero genera referencias
a las variables para ser más rápido incluso para variables con el mismo nombre pero diferente valor, por lo tanto, los valores numéricos son
inmutables para python ya que solo cambia la referencia en memoria, misma situación pasa para las cadenas de texto, son inmutables

Las tuplas también son inmutables, y se decalran asi: tupla = ('a', 2, 'b'), por lo que no puedo cambiar el valor de ellas

Los tipos mutables son por ejemplos las listas, es decir, miLista =[1,2,3] y puedo agregar valores o cambiando tipo milista[0] = 'a' y la posicion
cero cambiará por una 'a'

Si queremos añadir elementos usamos el metodo append, para eliminar usamos remove, para unir dos listas podemos usar append para que quede como
lista anidada

Los diccionarios también son mutables, y parecen json, y se declaran con {}, y deben tener una clave y un valor, y podemos cambiar los valores del
diccionario

Para eliminar las claves podemos usar el método pop o el método popitem que borra el ultimo elemento

También tenemos conjuntos o sets, que son listas que no permiten duplicados de los elementos y se declaran con llaves sin tener elementos clave valor

Los conjuntos tienen también operaciones matemáticas por ejemplo unir dos conjuntos seria a | b lo que dará el resultado de la unión de a y b sin
tener resultados
La interseccion es a & b
La diferencia es con a - b, los valores que no están ni en a ni en b
Diferencia simetrica a ^ b 
"""
