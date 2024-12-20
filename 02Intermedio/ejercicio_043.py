'''
### RECREACIÓN DE LA FUNCIÓN MIN ###
Escribe una función minimo(L) que tome unalista de enteros L como
parámetro y devuelva el valor más pequeño.

Pruebas de verificación:
minimo ([-9, 2, 4, 1, 8]) => -9
minimo ([-3, 1, 7, 6, -2, 3]) => -3
'''

L1 = [-9, 2, 4, 1, 8]
L2 = [-3, 1, 7, 6, 2, 3]

def minimo (L):
    minimo = L[0]
    for i in (0, len(L)-1):        
        if L[i] < minimo:
            minimo = L[i]
    return minimo

print (f"El valor mínimo de la lista {L1} es el {minimo(L1)}")
print (f"El valor mínimo de la lista {L2} es el {minimo(L2)}")