'''
### ELIMINAR ESPACIOS EU UN FRASE ###
Escribir una función llamada eliminarEsp(frase) que tome como
parámetro una frase en forma de cadena de caracteres y devuelva esa
misma frase sin los espacios (si los hay) entre las palabras.

Pruebas de verificación:
eliminarEsp ("Francia es hermosa.") => Franciaeshermosa.
eliminarEsp ("Me llevaré mi bicicleta") => Mellevarémibicicleta.
'''

def eliminarEsp (frase):
    newFrase = ""
    for i in frase: # Recorremos la frase
        if i != " ": # Si el caracter no es un espacio
            newFrase += i # Lo añadimos a la nueva frase

    return newFrase

frase = input ("Introduzca una frase a la que eliminarle los espacios: ")
print (eliminarEsp (frase))