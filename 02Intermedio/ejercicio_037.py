'''
### SUMA DE UNA LISTA ###
Escribe una función calcularSuma (L) que tome una lista de enteror L
como parámetro y devuelva la suma de los elementos de la lista.

Pruebas de verificación:
calcularSuma([3, 2, 6, 9, -1, 5]) => 24
calcularSuma ([-3, -6, 0, 1, 2, 7]) => 1
'''

def calcularSuma (L):
    return sum(L) # Suma de los elementos de la lista L y se guarda en la variable suma
    
print(calcularSuma([3, 2, 6, 9, -1, 5])) # 24
print(calcularSuma([-3, -6, 0, 1, 2, 7])) # 1