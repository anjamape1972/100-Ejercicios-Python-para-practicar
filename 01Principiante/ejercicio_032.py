'''
Escribir un programa que cree la variable L y le asigne la
lista [3, 6, 9, 12, 15, 18, 21, 24]. Luego, crear una nueva
lista L1 mediante una comprensión de listas, que contenga los
números L divididos por 3. El programa dee mostrar la lista L1
en la consola.
'''

L = []

for i in range (3, 25, 3):
    L.append(i)
print(L)

L1 = [int (i/3) for i in L]
print(L1)