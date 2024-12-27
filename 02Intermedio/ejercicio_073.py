'''
En este ejercicio, retomaremos la solución del ejercicio 37 que consiste en
escribir una función calcularSuma(L).
El objetivo del ejercicio es recrear la misma función, pero esta vez de manera
recursiva.
'''

def calcularSuma (L):
    if len (L) == 0: # Si la longitud de la lista es 0,
        return 0 # Devuelve 0
    return L [0] + calcularSuma (L[1:]) # Devuelve el primer elemento de la lista L y se suma con el resultado de la función calcularSuma con el resto de la lista L

Lista1 = [1, 2, 3]
Lista2 = []

print (calcularSuma (Lista1))
print (calcularSuma (Lista2))