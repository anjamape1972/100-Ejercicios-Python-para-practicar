'''
### RECREACIÓN DEL MÉTODO JOIN ###
Escribir una función join(L, caracter) que permita transformar una lista L en
una cadena de caracteres con el separador aracter pasado como parámetro.

Pruebas de verificación:
join(["Hola", "Aurélie"], " ") => "Hola Aurélie"
join (["Hola", "¿Está bien?"], ".") = "Hola.¿Está bien?"
'''

def join (L, caracter):
    newString = "" # Inicializamos la variable que contendrá la cadena
    for i in range (len (L)): # Recorremos la lista L
        newString += L[i] # Añadimos el elemento de la lista a la cadena
        if i < len(L)-1: # Si no es el último elemento de la lista
            newString += caracter # Añadimos el caracter separador
    return newString

print (join(["Hola", "Aurélie"], " "))
print (join (["Hola", "¿Está bien?"], "."))