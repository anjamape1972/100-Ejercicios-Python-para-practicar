'''
Escribir una función codigoSuma(numero) que toma como parámetro
un número entero numero estrictamente mayor que 100 y permite
determinar un código a partir de este número, siguiendo los siguientes
paso:
    - Paso 1: Suma de los dígitos del número introducido en el parámetro.
    - Paso 2: Repite el cálculo de la suma obtenida (en el paso 1)
            siempre que no esté entre 1 y 9.
    
El código será el número pasado como parámetro al que añadimos la
última suma obtenida a su izquierda.

Pruebas de verificación:
codigoSuma (69810) => 669810
codigoSuma (3201) => 63201
'''

def sumarDigitos (numero): # Función aux para sumar los dígitos de un número
    strNumero = str (numero) # Convertir el número en string
    listDigitos = [] # Lista para guardar los dígitos
    sumaLista = 0 # Variable para guardar la suma de los dígitos
    for i in range (len (strNumero)): # Recorrer el número
        listDigitos.append (strNumero [i]) # Añadir cada dígito a la lista
        listDigitos [i] = int (listDigitos [i]) # Convertir cada dígito en entero
        sumaLista = sum (listDigitos) # Sumar los dígitos
    return sumaLista # Retornar la suma

def codigoSuma (numero): # Función principal para determinar el código
    if numero >= 100: # Condición para que el número sea >= 100
        resultado = sumarDigitos (numero) # Llamar a la función auxiliar
        if resultado >= 10: # Condición para que la suma sea >= 10
            resultado = sumarDigitos (resultado) # Llamar a la función auxiliar
        strNumero = str (numero) # Convertir el número en string
        strResultado = str (resultado) # Convertir la suma en string
        strCodigo = strResultado + strNumero # Concatenar la suma con el número
        codigo = int (strCodigo) # Convertir el código en entero
        return codigo # Retornar el código
    return "No se cumple la condición requerida de que el número sea >= 100." # Mensaje de error si no se cumple la condición

print (codigoSuma (69810))
print (codigoSuma (3201))
print (codigoSuma (99))