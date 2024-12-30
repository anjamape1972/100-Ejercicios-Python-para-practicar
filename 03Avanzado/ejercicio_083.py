'''
### NOMBRE CON DÍGITOS DISTINTOS ###
Escribir una función esDistinto(numero) que toma como parámetro un
número entero y verifica si todos los dígitos de este número son
diferentes. La función debe devolver True si el número contiene dígitos
todos distintos y False en caso contrario.

Pruebas de verificación:
esDistinto (9647) => True
esDistinto (1343) => False
'''

def esDistinto (numero):
    strNumero = str (numero) # Convertimos el número a string
    listDigitos = [] # Creamos una lista vacía
    for digito in strNumero: # Recorremos el número convertido a string
        listDigitos.append (digito) # Añadimos cada dígito a la lista
    if len (listDigitos) == len (set (listDigitos)): # Comparamos la longitud de la lista con la longitud de la lista convertida a set
        return True # Si son iguales, devolvemos True
    return False # Si no, devolvemos False

        

print (esDistinto (9647))
print (esDistinto (1343))