'''
### NÚMERO DE OCURRENCIAS DE UNA PALABRA EN UN ARCHIVO ###
Escribir una función numOcFichero(rutaFichero, palabra) que tome como
parámetros la ruta del fichero rutaFichero y una palabra. La función debe
devolver el número de veces que la palabra aparece en el fichero pasado
como parámetro.
'''

def numOcFichero (rutaFichero, palabra):
    fichero = open (rutaFichero, "r+") # Abre el fichero en modo lectura y escritura
    contenido = fichero.read () # Lee el contenido del fichero
    listContenido = contenido.split () # Divide el contenido en una lista de palabras
    contador = 0
    for element in listContenido: # Recorre cada elemento de la lista
        if str (element) == palabra: # Si el elemento es igual a la palabra
            contador += 1 # Aumenta el contador
    fichero.close () # Cierra el fichero
    return f"El número de veces que aparece la palabra '{palabra}' es de {contador}."

rutaFichero = input ("Por favor, indique la ruta del fichero: ")
palabra = input ("Por favor, indique la palabra de la que desea saber el número de repeticiones: ")
print (numOcFichero (rutaFichero, palabra))