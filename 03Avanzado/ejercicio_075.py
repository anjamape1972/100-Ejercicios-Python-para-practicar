'''
### FUNCIONES RECURSIVAS MUTUAS ###
Un número n es par si n-1 es impar, y viceversa, si un número n es impar,
entonces n-1 es par.
Escribir dos funciiones recursivas mutuas, numeroPar(n) y numeroImpar(n),
que permitan saber si un numero n es par o impar.

Pruebas de verificación:
numeroPar (5) => False
numeroImpar (7) => True
'''

def numeroPar(numero):
    if numero == 1:  # Caso base: 1 es impar
        return False
    return numeroImpar(numero - 1)  # Llamada recursiva

def numeroImpar(numero):
    if numero == 1:  # Caso base: 1 es impar
        return True
    return numeroPar(numero - 1)  # Llamada recursiva


print (numeroPar (5))
print (numeroImpar (7))
