'''
### FUNCIÓN TRIGONOMÉTRICA ###
Escribe una función funcTrigo(x) que tome un número x como parámetro y
devuelva el resultado de la función f(x) = cos(x)*sin(x) + sin(x) + 8.

Nota: en este ejercicio vamos a utilizar el módulo math.

Pruebas de verificación:
funcTrigo (math.pi/4) => 9.207106781186548
funcTrigo (math.pi) => 8
'''

import math

def funcTrigo (x):
    resultado = math.cos(x)*math.sin(x) + math.sin(x) + 8
    return resultado

print (funcTrigo (math.pi/4))
print (funcTrigo (math.pi))