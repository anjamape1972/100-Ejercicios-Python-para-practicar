'''
### recreación de la función max ###
Escribe una función maximo(L) que tome una lista de enteros como
parámetro y devuelva el valor máximo de la lista.

Nota: La idea es que no utilices la función max de Python.

Pruebas de verificación:
maximo ([-9, 2, 4, 1, 8]) => 8
maximo ([-3, 1, 7, 6, 2, 3]) => 7
'''

def maximo(L):
    maximo = L[0]
    for i in L:
        if i > maximo:
            maximo = i
    return maximo

L1 = [-9, 2, 4, 1, 8]
L2 = [-3, 1, 7, 6, 2, 3]
print(f"El valor máximo de la lista {L1} es el {maximo(L1)}")
print(f"El valor máximo de la lista {L2} es el {maximo(L2)}")
