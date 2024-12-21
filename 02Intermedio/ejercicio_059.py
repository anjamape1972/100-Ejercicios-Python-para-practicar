'''
### UNIÓN DE LISTAS SIN DUPLICACIÓN ###
Escribir una función unionLista(L1, L2, L3) que toma como parámetros
tres listas de enteros L1, L2, L3, y evuelve una lista de orden
ascendente que representa la unión de estas tres listas sin duplicación
de números.

Pruebas de verificación:
unionLista ([3, 6, 9, 3], [1, 0, 3], [12, 6, 0]) => [0, 1, 3, 6, 9, 12]
unionLista ([7, 44, -3], [], [7, 2, 7]) => [-3, 2, 7, 44]
'''

def unionLista (L1, L2, L3):
    unionListas = L1 + L2 + L3 # Concatenación de listas
    setListas = set (unionListas) # Eliminación de duplicados
    newLista = list (setListas) # Transformación a lista
    return sorted (newLista) # Orden ascendente

print (unionLista ([3, 6, 9, 3], [1, 0, 3], [12, 6, 0]))