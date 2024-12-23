'''
### ESCRIBIR UN FICHERO ###
Escribir una función escribirFichero(nomFichero, texto) que tome como
parámetros el nombre del archivo nomFichero y el texto que queremos escribir
en el fichero. La función nos permitirá al final tener un archivo que contenga
el texto pasado como parámetro.

Pruebas de verificación:
escribirFichero ("prueba.txt", "Hola, me llamo Antonio Javier y tengo 52 años".)
'''

def escribirFichero (nomFichero, texto):
    with open (nomFichero, "w+") as prueba: # with open es para abrir el archivo y cerrarlo automáticamente, "w+" es para escribir en el archivo
        prueba.write (texto) # Escribimos el texto en el archivo

nomFichero = input ("Indique el nombre del archivo (con su ruta de directorios y extensión): ")
texto = "Hola, me llamo Antonio Javier y tengo 52 años"
escribirFichero (nomFichero, texto)