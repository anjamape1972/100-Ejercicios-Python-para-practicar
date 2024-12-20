'''
Escribir la instrucción que permite crear una lista de
números del 1 al 10 utilizando una comprensión de lista.
'''

### Modo 1 ###
lista = []
for i in range (1, 11):
    lista.append (i)
print (lista)

### Modo 2 ###
lista2 = [j for j in range (1, 11)]
print (lista2)