'''
### CALCULAR LA MEDIA DE UNA LISTA ###
Escribe una función mediaLista(L) que tome como parámetro una
lista de enteros y devuelva la media de la lista.

Pruebas de verificación:
mediaLista ([1, 2, 3, 4, 5, 6, 7]) => 4.0
mediaLista ([3, 0, -1, 5, 6, 9, 17]) => 5.571428571428571
'''

def mediaLista (L):
    media = sum (L) / len (L) # Suma de los elementos de la lista dividido por la cantidad de elementos
    return media

print (mediaLista ([1, 2, 3, 4, 5, 6, 7]))
print (mediaLista ([3, 0, -1, 5, 6, 9, 17]))