'''
### NÚMERO DE ARCHIVOS EN UNA CARPETA ###
Escribir una función nombreFichero(rutaDirectorio) que toma como parámetros
la ruta del directorio rutaDirectorio y devuelve el número de ficheros
conenidos en el directorio pasado como parámetro.
'''

import os # Importamos el módulo os para trabajar con el sistema operativo

def nombreFichero (rutaDirectorio):
    counter = 0
    listDirectory = os.listdir (rutaDirectorio) # Listamos los elementos del directorio
    for element in listDirectory: # Recorremos los elementos del directorio
        if os.path.isfile (os.path.join (rutaDirectorio, element)): # Si el elemento es un archivo. Con os.path.join unimos la ruta del directorio con el nombre del archivo
            counter += 1 # Aumentamos el contador
    return counter

rutaDirectorio = input ("Indique la ruta del directorio para contar archivos: ")
print (nombreFichero(rutaDirectorio))