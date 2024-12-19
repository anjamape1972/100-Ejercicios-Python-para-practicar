'''
ORDENAR UNA LISTA DE TUPLAS
Escriba un programa que permita ordenar una lista de tuplas L
en orden ascendente, basándose en el segundo elemento de la tupla.
La lista que consideraremos en este ejercicio es:
L = [("Manzana", 15), ("Banana", 8), ("Fresa", 12), ("Kiwi", 9), ("Melocotón", 2)]

La lista L que debemos obtener será la siguiente:
L = [("Melocotón", 2), ("Banana", 8), ("Kiwi", 9), ("Fresa", 12), ("Manzana", 15)]
'''

L = [("Manzana", 15, 3.5), ("Banana", 8, 7), ("Fresa", 12, 87), ("Kiwi", 9, 2), ("Melocotón", 2, -1)]

L.sort (key= lambda x: x[1]) # lambda es una función anónima que usamos para indicar que queremos ordenar por el segundo elemento de la tupla
print (L)

### Esto no viene en el enunciado del ejercicio ###
L.sort (key= lambda x: x[0]) # lambda es una función anónima que usamos para indicar que queremos ordenar por el primer elemento de la tupla
print (L)

L.sort (key= lambda x: x[2]) # lambda es una función anónima que usamos para indicar que queremos ordenar por el tercer elemento de la tupla
print (L)