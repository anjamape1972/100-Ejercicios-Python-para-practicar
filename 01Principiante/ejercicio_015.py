'''
Escribir un programa que cree la lista L asignándole el
valor [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] y luego crear una nueva
lista L1 que recupera un elemento de cada tre de la lista L.
En este caso, debemos obtener al final la siguiente lista:
[1, 4, 7, 10]
'''

### Modo 1 ###
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L1 = []

for i in range (0, len (L), 3):
    L1.append (L[i])

print (L1)

### Modo 2 ###
L2 = [L[i] for i in range (len(L)) if i % 3 == 0]

print (L2)