'''
Escribir un programa que permita eliminar un elemento de una
lista. Consideremos la lista L = [1, 2, 3, 4, 5] y queremos
eliminar el número 1. El resultado sería L = [2, 3, 4, 5].
'''

L = [1, 2, 3, 4, 5]
L.remove(1)
print(L)

# Otra forma
L = [1, 2, 3, 4, 5]
delNum = int (input ("Ingrese el número a eliminar: "))
L.remove(delNum)
print(L)