'''
Escribir as instrucciones que permiten crear una lista vacía L
y agregarle los enteros 10, 25, 30, 45, 90 y las cadenas de caracteres
"ab", "cd", "ef".
'''

### Modo 1 ###
L = []

L.append (10)
L.append (25)
L.append (30)
L.append (45)
L.append (90)
L.append ("ab")
L.append ("cd")
L.append ("ef")

print (L)

### Modo 2 ###
L2 = []

elements_to_add = [10, 25, 30, 45, 90, "ab", "cd", "ef"]
for i in elements_to_add:
    L2.append (i)

print (L2)