'''
Escriba un programa que permita mezclar aleatoriamente los
elementos de una lista L.
Tomemos por ejemplo la lista L = [3, 6, 8, 7, 2, "s", "ch", "d"]
'''

import random

L = [3, 6, 8, 7, 2, "s", "ch", "d"]

print (L)
random.shuffle(L) # Mezcla los elementos de la lista en la misma lista, no crea una nueva lista
print (L)

newList = random.sample(L, len(L)) # Mezcla los elementos de la lista y crea una nueva lista
print (newList)