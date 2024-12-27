'''
Escribir un programa que permita almacenar en una lista L todos los enteros
positivos de tres dígitos de la forma abc tal que, para cada entero, la suma de
sus digítos a+b+c sea un divisor del producto de sus dígitos a*b*c.
El programa debe mostrar al final la lista que contiene estos enteros.

Por ejemplo: el número 514 cumple con esta propiedad, 5+1+4 = 10 es un
            divisor de 5*1*4 = 20
'''

import math

L = []
for i in range (100, 1000): # Rango de 100 a 999 (3 digitos)
    digitos = [int(d) for d in str(i)] # Convertir el numero a una lista de digitos (int)
    if ((math.prod (digitos) % sum (digitos)) == 0 and math.prod (digitos) != 0): # Si el producto de los digitos es divisible por la suma de los digitos y el producto no es 0
        print (i)