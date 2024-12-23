'''
### LECTURA DE UN FICHERO ###
Escribir una función leerFichero(rutaFichero) que toma como parámetro la
ruta completa del fichero rutaFichero y devuelve su contenido. El contenido
del fichero debe mostrarse en consola.

Nota: para este ejercicio, tendría que crear un fichero de texto con contenido
para probar su función.

pruebas de verificación:
leerFichero ("C:prueba.txt") => El contenido del fichero
'''

def leerFichero (rutaFichero):
    fichero = open (rutaFichero, "r+") # Abre el archivo. r+ para lectura y escritura (no sobreescribe)
    contenido = fichero.read() # Lee el contenido del archivo y lo guarda en la variable contenido
    fichero.close () # Cierra el archivo
    return contenido # Devuelve el contenido del archivo

rutaFichero = input ("Indique la ruta del fichero que quiere leer: ") # Solicita la ruta del archivo
print (leerFichero (rutaFichero))