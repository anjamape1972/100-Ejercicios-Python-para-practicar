'''
### FUNCIÓN MATEMÁTICA ###
Escribe una función llamada f(a, b, x) tomando como parametros 3 enteros a, b, x
y devuelve el resultado de la siguiente función:

f(a, b, x) = a*(x**3) + 2*a*(x**2) + b

Pruebas de verificación:
f(3, 0, 1)
9

f(0, 2, 2)
2
'''

def f(a, b, x):
    return a*(x**3) + 2*a*(x**2) + b

print(f(3, 0, 1))
print(f(0, 2, 2))