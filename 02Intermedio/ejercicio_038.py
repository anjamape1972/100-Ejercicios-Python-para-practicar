'''
### ELIMINACIÓN DE DUPLICADOS ###
Escribe una función eliminarDuplicados (L) que tome una lista de enteros L
como parámetro y devuelva una lista sin duplicados en orden ascendente.

Pruebas de verificación:
eliminarDuplicados ([0,3,5,7,3,5,1,-1]) => [-1, 0, 1, 3, 5, 7]
eliminarDuplicados ([0,5,9,10,3.2,1,-3]) => [-3, 0, 1, 3.2, 5, 9, 10]
'''

import random

def eliminarDuplicados(L):
    return sorted(list(set(L)))

print(eliminarDuplicados([0,3,5,7,3,5,1,-1])) # [-1, 0, 1, 3, 5, 7]
print(eliminarDuplicados([0,5,9,10,3.2,1,-3])) # [-3, 0, 1, 3.2, 5, 9, 10]

# Igual que el ejercicio anterior, pero en orden descendente
def eliminarDuplicadosReverse (L):
    return sorted(list(set(L)), reverse=True)

print(eliminarDuplicadosReverse([0,3,5,7,3,5,1,-1])) # [7, 5, 3, 1, 0, -1]
print(eliminarDuplicadosReverse([0,5,9,10,3.2,1,-3])) # [10, 9, 5, 3.2, 1, 0, -3]

# Igual que el ejercicio anterior, pero en orden aleatorio (random) y sin duplicados en la lista
L = [0,3,5,7,3,5,1,-1]
L1 = [0,5,9,10,3.2,1,-3]
def eliminarDuplicadosRandom (L):
    return random.sample(list(set(L)), len(list(set(L))))

print (eliminarDuplicadosRandom(L)) # None
print (eliminarDuplicadosRandom(L1)) # None