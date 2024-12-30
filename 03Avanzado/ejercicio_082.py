'''
### LOS NÚMEROS PRIMOS CIRCULARES ###
Escribir una función esCirculoPrimo(numero) que toma como parámetro un
número entero numero y verifica si es un número circular primo. La función
devuelve True si el número pasado como parámetro es un número circular
primo y False en caso contrario.

Recordatorio: un número es un número circular primo si la rotación de sus
dígitos son números primos. Por ejemplo, el número 197 es un número circular
primo ya que 197, 971 y 719 son números primos.
Otros números circulares primos: 19391, 19937, 71, 37, 31, 9377.

Indicación: se recomienda implementar una función esPrimo(numero) que
verifique si un número es primo, y luego usarla en esCirculoPrimo(numero).

Pruebas de verificación:
esCirculoPrimo (9377) => True
esCirculoPrimo (36) => False
'''

def esPrimo (numero): # Función que verifica si un número es primo
    if numero <= 1: # Si el número es menor o igual a 1, no es primo
        return False # Retornamos False
    for i in range (2, int (numero ** 0.5) + 1): # Recorremos los números desde el 2 hasta la raíz cuadrada del número
        if numero % i == 0: # Si el número es divisible por i, no es primo
            return False # Retornamos False
    return True # Si no se cumple la condición anterior, el número es primo

def esCirculoPrimo (numero): # Función que verifica si un número es un número circular primo
    numCirculares = [] # Lista para almacenar los números circulares
    strNumero = str (numero) # Convertimos el número a cadena
    for i in range (len (strNumero)): # Recorremos la longitud de la cadena
        newStrNumero = strNumero [-1] + strNumero [:-1] # Rotamos los dígitos del número y lo almacenamos en una nueva variable
        numCirculares.append (newStrNumero) # Agregamos el número circular a la lista
        strNumero = newStrNumero # Actualizamos el número
    for i in range (len (numCirculares)): # Recorremos la longitud de la lista
        numCirculares [i] = int (numCirculares [i]) # Convertimos los números circulares a enteros
        if esPrimo (numCirculares [i]): # Si el número circular es primo
            return True # Retornamos True
    return False # Si no se cumple la condición anterior, retornamos False

print (esCirculoPrimo (9377))
print (esCirculoPrimo (36))