'''
Escriba un programa que, dadas dos listas L1 y L2, devuelva
una lista L3 que contenga los elementos en común entre L1 y L2.

Para probar, vamos a tomar las listas:
L1 = [9, 8, 7, 14, 3, 2, "a", "p", "hola", "b"]
L2 = ["b", 1, 9.2, 6, 3, 9, "p"]
'''

L1 = [9, 8, 7, 14, 3, 2, 2, "a", "p", "hola", "b"]
L2 = ["b", 1, 9.2, 6, 3, 2, 2, 9, "p"]

# De esta forma, si hay elementos repetidos dentro de las listas, salen repetidos en la nueva lista
L3 = [elemento for elemento in L1 if elemento in L2]
print (L3)

# Aquí convertimos las listas en sets (que no tienen elementos repetidos), para evitar que
# salgan elementos repetidos en la nueva lista
L4 = (set (L1).intersection(set(L2)))
L4 = list (L4)
print (L4)