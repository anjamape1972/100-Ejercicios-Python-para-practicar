'''
### NÚMEROS PALÍNDROMOS ###
Escribir una función esUnPalindromo(numero) que tome como parámetros un
número entero numero y devuelva True si numero es un palíndromo y False
si no lo es.

Recordatorio: Un número palíndromo es un número natural mayos que 10, que
leído de izquierda a derecha o de derecha a izquierda, proporciona el mismo
número.

Por ejemplo: los números 69596, 5231324, 212 son números palíndromos.

Pruebas de verificación:
esUnPalindromo (10) => False
esUnPalindromo (919) => True
'''

def esUnPalindromo (numero):
    strNumero = str (numero) # Convertimos el número a string para poder recorrerlo
    for i in range (len (strNumero)): # Recorremos el número
        if strNumero [i] != strNumero [-(i+1)]: # Comparamos el número de izquierda a derecha con el de derecha a izquierda
            return False
    return True

# print (esUnPalindromo (10))
# print (esUnPalindromo (919))
# print (esUnPalindromo(881118))