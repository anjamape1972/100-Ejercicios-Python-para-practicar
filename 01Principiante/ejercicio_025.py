'''
Escribir un programa que muestre la carpeta en la que se encuentra
el script Python actual.
'''
import os

print (os.getcwd())
print (os.path.dirname(os.path.abspath(__file__))) # Otra forma de hacerlo