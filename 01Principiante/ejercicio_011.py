'''
Escribir la instrucción que permite crear una lista de números
pares del 1 al 10 con una comprensión de lista
'''

### Modo 1 ###
lista = [i+1 for i in range (1, 11, 2)]
print (lista)

### Modo 2 ###
lista2 = [j for j in range (1, 11) if j % 2 == 0]
print (lista2)