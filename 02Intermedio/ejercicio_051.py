'''
### CÁLCULO DEL FACTORIAL DE UN NÚMERO ###
Escribir una función llamada calculoFactorial(n) que permita calcular
el factorial de un número (en el sentido matemático) y devuelva el
resultado obtenido al final de este cálculo.

Pruebas de verificación:
calculoFactorial (3) => 6
calculoFactorial (9) => 362880
calculoFactorial (0) => 1
'''

def calculoFactorial (n):
    fact = 1
    if n < 0:
        return f"Los números negativos como el {n} no tienen factorial."
    elif n == 0 or n == 1:
        return f"El factorial de {n} es 1."
    else:
        for i in range (2, n+1): # Se inicia en 2 porque el factorial de 0 y 1 es 1. Y termina en n+1 porque el rango no incluye el último número.
            fact *= i
        return f"El factorial de {n} es {fact}."
    
print (calculoFactorial (9))
print (calculoFactorial (3))
print (calculoFactorial (1))
print (calculoFactorial (0))
print (calculoFactorial (-1))