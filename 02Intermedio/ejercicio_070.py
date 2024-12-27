'''
### GENERAR UNA CONTRASEÑA ALEATORIA ###
Escribir una función generarContraseña(caracteres, longitud) que tome como
parámetros una lista de caracteres caracteres y la longitud de la contraseña
longitud, y luego genere aleatoriamente una contraseña con la longitud y
caracteres pasados como parámetros. La función debe devolver la contraseña
en forma de una cadena de caracteres.
'''

import random

def generarContraseña (caracteres, longitud):
    password = "" # Inicializamos la variable password
    for i in range (longitud): # Recorremos la longitud de la contraseña
        indice = random.randint(0, len (caracteres)-1) # Generamos un número aleatorio entre 0 y la longitud de la lista de caracteres
        element = caracteres [indice] # Obtenemos el elemento de la lista de caracteres en la posición del número aleatorio
        password += element # Añadimos el elemento a la variable password
    return password

listaCaracteres = ["a", "1", "d", "8", "t", "5", "6", "3", "8"]

print (generarContraseña (listaCaracteres, 6))