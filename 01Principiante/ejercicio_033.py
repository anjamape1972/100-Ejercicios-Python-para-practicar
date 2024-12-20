'''
Cree un programa para crear la variable L, asignarle la lista
[-6, 5, -3, -1, 2, 8, -3.6], luego crear una nueva lista L1 usando
comprensión de lista con los numeros de L que son estrictamente
mayores que 0 y finalmente mostrar la lista L1 en la consola.
'''

L = [-6, 5, -3, -1, 2, 8, -3.6]

L1 = [i for i in L if i > 0]
print(L1)