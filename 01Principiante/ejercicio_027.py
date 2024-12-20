'''
Escribir un programa que permita recuperar la extensión
de un archivo.
'''
import os

def extension_archivo(archivo):
    return os.path.splitext(archivo)[1] # Devuelve una tupla con la ruta del archivo y la extensión. Con [1] se obtiene la extensión.

archivo = "archivo.txt"
print(extension_archivo(archivo)) # .txt
archivo = "imagen.png"
print(extension_archivo(archivo)) # .png
archivo = "archivosinextension"
print(extension_archivo(archivo)) # ''
archivo = "archivo.con.muchas.extensiones.pdf"
print(extension_archivo(archivo)) # .pdf