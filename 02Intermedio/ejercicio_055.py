'''
### POSICIÓN DE UN ELEMENTO EN UNA LISTA ###
Escribir una función llamada posicionEltLista(L, x) que tome como
parámetros una lista de elementos L y un elemento x, y devuelva el
índice (o los índices) donde se encuentra el elemento x en la lista L.
La función debe devolver una lista de índices. Si el elemento x no se
encuentra en la lista L, el programa mostrará en la consola: "El elemento
x no está en la lista L".

Pruebas de verificación:
posicionEltLista ([1, 2, 3, 6, 8, 7, 3], 3) => [2, 6]
posicionEltLista ([6, 8, 9, 3, 7], -1) = El elemento -1 no está en la lista [6, 8, 9, 3, 7]
'''

def posicionEltLista (L, x):
    listIndex = [] # Lista de índices
    for i in range (len(L)): # Recorre la lista
        if x == L[i]: # Si el elemento x está en la lista L
            listIndex.append (i) # Añade el índice a la lista de índices
        else: # Si el elemento x no está en la lista L
            return f"El elemento {x} no está en la lista {L}"
    return listIndex

print (posicionEltLista ([1, 2, 3, 6, 8, 7, 3], 3))
print (posicionEltLista ([6, 8, 9, 3, 7], -1))