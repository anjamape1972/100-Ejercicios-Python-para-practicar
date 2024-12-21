'''
### CONCATENACIÓN DE LISTAS ###
Escribe una función concatListas (L1, L2, L3) que tome tres listas
L1, L2 y L3 como parámetros y devuelva la concatenación de las
tres listas.

Pruebas de verificación:
concatListas ([0, 9, 8], [2, 6, 9], [True, False, "abc"]) => [0, 9, 8, 2, 6, 9, True, False, "abc"]
concatListas ([[38, -1], 3, -9], ["xz", "Francia"], []) = [[38, -1], 3, -9, "xz", "Francia"]
'''

def concatListas (L1, L2, L3):
    newList = L1 + L2 + L3
    return newList

print (concatListas ([0, 9, 8], [2, 6, 9], [True, False, "abc"]))
print (concatListas ([[38, -1], 3, -9], ["xz", "Francia"], []))