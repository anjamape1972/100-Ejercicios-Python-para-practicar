'''
### NÚMERO DE APARICIONES EN UNA LISTA ###
Escribe una función numeroOcurrencias(L) que tome como parámetros
una lista L y devuelva una lista de tuplas donde cada tupla corresponde
a un elemento de la lista L con su número de ocurrencias en la lista.

Pruebas de verificación:
numeroOcurrencias ([-4, 8, -3, 2, 1, 2, 7, 9, -3, 8, 1]) =>
    => [(-4, 1), (8, 2), (-3, 2), (2, 2), (1, 2), (7, 1), (9, 1)]
numeroOcurrencias (["a", 3, 4, "b", "a", 3]) =>
    => [("a", 2), (3, 2), (4, 1), ("b", 1)]
'''

def numeroOcurrencias (L):
    listaResultante = []
    for elemento in L: # Recorre cada elemento de la lista
        numOcu = L.count (elemento) # Cuenta cuantas veces aparece el elemento en la lista
        tuplaDeElemento = (elemento, numOcu) # Crea una tupla con el elemento y el número de ocurrencias
        if tuplaDeElemento not in listaResultante: # Si la tupla no está en la lista resultante
            listaResultante.append (tuplaDeElemento) # Agrega la tupla a la lista resultante
    return listaResultante
        

print (numeroOcurrencias ([-4, 8, -3, 2, 1, 2, 7, 9, -3, 8, 1]))
print (numeroOcurrencias (["a", 3, 4, "b", "a", 3]))