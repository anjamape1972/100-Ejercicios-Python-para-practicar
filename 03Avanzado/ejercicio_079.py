'''
### RECREACIÓN DEL MÉTODO ISDIGIT () ###
Escribir una función isdigit(cadena) que permita verificar si la cadena es un
número o no. La función devuelve True si la cadena es un número y False si no
lo es.

Pruebas de verificación:
isdigit ("125920") => True
isdigit ("edgte9be") => False
'''

def isdigit (cadena):
    numbers = "1234567890" # Cadena con los números del 0 al 9
    for i in cadena: # Recorremos la cadena que nos pasan
        for j in numbers: # Recorremos la cadena con los números del 0 al 9
            if i == j: # Si el caracter de la cadena es igual a un número
                return True # Devolvemos True
            return False # Si no es un número devolvemos False
    
print (isdigit ("125920"))
print (isdigit ("edgte9be"))