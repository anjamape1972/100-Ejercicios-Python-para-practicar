'''
### SUPRIMIR UN CARÁCTER DE UN ARCHIVO ###
Escribir una función eliminarCaracter(rutaFichero, caracter) que toma como
parámetros la ruta del fichero rutaFichero y un carácter. La función debe
eliminar el carácter pasado como parámetro del fichero correspondiente.
'''

def eliminarCaracter (rutaFichero, caracter):
    fichero = open (rutaFichero, "r+") # Abrimos el fichero en modo lectura y escritura
    contenido = fichero.read () # Leemos el contenido del fichero
    newContenido = "" # Creamos una variable para el nuevo contenido
    for element in contenido: # Recorremos el contenido del fichero
        if element != caracter: # Si el carácter no es igual al carácter a eliminar
            newContenido += element # Añadimos el carácter al nuevo contenido
    fichero.close () # Cerramos el fichero
    return newContenido

rutaFichero = input ("Indique la ruta del fichero sobre el que trabajar: ")
caracter = input ("Indique el carácter que desea eliminar: ")
print (eliminarCaracter (rutaFichero, caracter))