'''
### PRESENCIA DE UN ELEMENTO EN UNA LISTA ###
Escribe una función llamada VerifPresencia (a, L) que toma como
parámetros una lista L y un elemento a. La función devuelve True si
el elemento a existe en la lista L y False en caso contrario.

Pruebas de verificación:
VerifPresencia(2, [1, 2, 3, 4, 5], 6) => True
VerifPresencia (-1, [3, 6, 9, 7, "abcr"]) => False
'''

def VerifPresencia (a, L):
    return a in L # Devuelve True si el elemento a existe en la lista L y False en caso contrario.

print(VerifPresencia(2, [1, 2, 3, 4, 5]))
print(VerifPresencia(-1, [3, 6, 9, 7, "abcr"]))