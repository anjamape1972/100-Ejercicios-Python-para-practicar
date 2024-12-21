'''
### RECREACIÓN DE LA FUNCIÓN LEN ###
Escribe una función longitud(L) que tome como parámetro una lista
de enteros L y devuelva el número de elementos de dicha lista.

Pruebas de verificación:
longitud ([3, 6, 7, "abde", [1, 3, 57], True]) => 6
longitud ([]) => 0
'''

def longitud (L): # Recibe una lista
    contador = 0
    for i in L: # Recorre la lista
        contador += 1 # Suma 1 al contador
    return contador

print (longitud ([3, 6, 7, "abde", [1, 3, 57], True]))
print (longitud ([]))