'''
### LOS NÚMEROS PALÍNDROMOS ###
El número palindrómico más grande obtenido como producto de dos números
de dos digítos es 0990 = 91 x 99.
Escribir un programa que encuentre el número palindrómigo más grande
obtenido como producto de dos números de tres dígitos.

Nota: Puede usar la función esUnPalindromo del ejercicio anterior.
'''
import ejercicio_080 # Importamos el ejercicio 080 para poder usar la función esUnPalindromo

listaResultados = [] # Creamos una lista vacía para almacenar los resultados

for i in range (100, 1000): # Recorremos los números de 100 a 999 (3 dígitos)
    for j in range (100, 1000): # Recorremos los números de 100 a 999 (3 dígitos)
        resultado = i * j # Multiplicamos los números de 3 dígitos
        if ejercicio_080.esUnPalindromo (resultado): # Si el resultado es un palíndromo
            listaResultados.append (resultado) # Añadimos el resultado a la lista

print (f"El número palindrómico más grande obtenido como producto\nde dos números de 3 dígitos es el {max (listaResultados)}.") # Imprimimos el número palindrómico más grande