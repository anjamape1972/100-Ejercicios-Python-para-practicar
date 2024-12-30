'''
### RECREACIÓN DEL MÉTODO SPLIT ###
Escriba una función split(frase, caracter) que convierta una sentencia en una
lista utilizando el separador de caracteres.

Pruebas de verificación:
split ("Hola Antonio Javier", " ") => ["Hola", "Antonio", "Javier"]
split ("Hola.¿Estás bien?", ".") => ["Hola", "¿Estás bien?"]
'''

def split (frase, caracter):
    listaPalabras = [] # Lista que contendrá las palabras de la frase separadas por el caracter
    palabra = "" # Variable que contendrá la palabra que se va a añadir a la lista
    for i in range (len (frase)): # Recorremos la frase caracter a caracter para separar las palabras
        if frase [i] != caracter: # Si el caracter no es el separador, añadimos el caracter a la palabra
            palabra += frase [i]
        else: # Si el caracter es el separador, añadimos la palabra a la lista y vaciamos la palabra
            listaPalabras.append (palabra) # Añadimos la palabra a la lista
            palabra = "" # Vaciamos la palabra
    if palabra: # Si la palabra no está vacía, la añadimos a la lista. Esto es porque al no estar el caracter al final de la frase, no se añadiría la última palabra
        listaPalabras.append (palabra) # Añadimos la palabra a la lista
    return listaPalabras


print (split ("Hola Antonio Javier", " "))
print (split ("Hola.¿Estás bien?", "."))