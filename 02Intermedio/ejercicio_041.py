'''
### SUMA DE UNA SUBLISTA ###
Escribir el código de la función sumaSublista (L, i, j) que toma 3 parámetros:
una lista L, un índice de inicio del cálculo i, y un índice de fin del cálculo j.
La función debe devolver la suma de los números que se encuentran entre los
índices i y j de la lista.

Pruebas de verificación:
sumaSublista ([4, 10, 12, 16, 18], 2, 4) => 46
sumaSublista ([2, 4, 6, 8, 10, 12], 0, 2) => 12
'''

def sumaSublista (L, i, j):
    suma = 0
    for x in range (i, j+1): # Recorre la sublista entre los índices i y j de la lista
        suma += L[x] # Suma los elementos de la sublista entre los índices i y j de la lista
    return suma

L1 = [4, 10, 12, 16, 18]
L2 = [2, 4, 6, 8, 10, 12]
print (sumaSublista (L1, 2, 4))
print (sumaSublista (L2, 0, 2))