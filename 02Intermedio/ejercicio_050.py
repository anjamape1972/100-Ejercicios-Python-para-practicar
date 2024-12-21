'''
### CONCATENACIÓN DE DICCIONARIOS ###
Escriba una función concatDicc(d1, d2) que tome dos diccionarios d1 y d2
como parámetros y devuelva la concatenación de estos dos diccionarios.

Pruebas de verificación:
concatDicc ({"a":3, "b":6}, {"c":2, "d":-1}) => {"a":3, "b":6, "c":2, "d":-1}
concatDicc ({"d":[2.9, 4.1]}, {"p":[]}) => {"d":[2.9, 4.1], "p":[]}
'''

def concatDicc (d1, d2):
    newDicct = d1 | d2 # Concatenación: Python 3.9 or higher version required for this operation
    return newDicct

# Otra forma de hacerlo:

def concatDicc2 (d1, d2):
    newDicct = d1.copy()
    newDicct.update(d2)
    return newDicct

d1 = {"a":3, "b":6}
d2 = {"c":2, "d":-1}
print (concatDicc (d1, d2))
print (concatDicc2 (d1, d2))

d1 = {"d":[2.9, 4.1]}
d2 = {"p":[]}
print (concatDicc (d1, d2))
print (concatDicc2 (d1, d2))