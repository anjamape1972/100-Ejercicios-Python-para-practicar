'''
### PRESENCIA DE UN NÚMERO EN UN FICHERO ###
Escribir una función presenciaNumero(rutaFichero) que toma como parámetro
la ruta del fichero rutaFichero y verifica si el fichero contiene un número.
La función de vuelve True si el fichero contiene un número y false en caso
contrario.
'''

def presenciaNumero (rutaFichero):
    fichero = open (rutaFichero, "r+")
    contenido = fichero.read ()
    for i in (contenido): # Recorremos el contenido del fichero
        if i.isdigit (): # Si el contenido es un número devolvemos True
            return True
    return False # Si no hay ningún número devolvemos False

rutaFichero = input ("Indique la ruta del fichero para comprobar si contiene números: ")
print (presenciaNumero (rutaFichero))