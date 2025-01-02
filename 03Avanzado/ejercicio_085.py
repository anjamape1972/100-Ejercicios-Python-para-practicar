'''
### BÚSQUEDA DICOTÓMICA ###
Escribir una función busquedaDicotomica(L, elt) que toma como
parámetros una lista L ordenada en orden ascendene y un elemento
elt. La función nos permite encontrar el elemento elt en la lista L
mediante una búsqueda dicotómica. Si el elemento es encontrado,
entonces la función devuelve true, de lo contrario devuelve False.

Pruebas de verificación:
busquedaDicotomica ([6, 9, 15, 36, 41, 43, 47], 41) => True
busquedaDicotomica ([-9, -1, 3, 4, 7, 11], 0) => False

Recordemos el algoritmo de búsqueda dicotómica:

Contexto: en una lista L ordenada de valores, se busca determinar si un
valor elt está presente en la lista L.

Pasos para la búsqueda por dicotomía:
    - Se toma el elemento del medio de la lista L y se compara con elt.
    - Si son iguales, el algoritmo se detiene y se encuentra el elemento.
      De lo contrario, se continúa la búsqueda en la primera o segunda
      mitad del arreglo.
    - Si al final se ha reducido la porción de la lista al punto de que no
      contiene ningún elemento, la búsqueda se detiene sin éxito: elt no
      está en L.
'''

def busquedaDicotomica (L, elt):
    sorted (L)
    if len (L) == 0:
        return False
    else:
        mitad = len (L) // 2
        if L [mitad] == elt:
            return True
        else:
            if elt < L [mitad]:
                return busquedaDicotomica (L [:mitad], elt)
            else:
                return busquedaDicotomica (L [mitad + 1:], elt)

print (busquedaDicotomica ([6, 9, 15, 36, 41, 43, 47], 9))
print (busquedaDicotomica ([-9, -1, 3, 4, 7, 11], 0))