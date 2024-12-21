'''
### DIVISORES DE UN NÚMERO ENTERO ###
Escribe una función divisor(n) que tome un entero n como parámetro
y devuelva una lista que contenga todos los divisores positivos
de n en orden ascendente.

Pruebas de verificación:
divisor (3) => [1, 3]
divisor (9) => [1, 3, 9]
'''

def divisor (n):
    lista_divisores = []
    for i in range (1, n+1): # Se agrega 1 para que el rango incluya el número n en la lista de divisores
        if n % i == 0: # Si el residuo de la división de n entre i es 0, entonces i es divisor de n
            lista_divisores.append (i) # Se agrega el divisor a la lista de divisores
    return lista_divisores

n = int (input ("Ingrese un número entero: ")) # Se solicita al usuario que ingrese un número entero
print (divisor (n)) # Se imprime la lista de divisores del número ingresado por el usuario