'''
### RECREACIÓN DEL MÉTODO REPLACE ###
Escribir una función reemplazar(frase, palabra, nuevaPalabra) que permita
reemplazar en la cadena de caracteres frase, la palabra introducida en el
segundo parámetro por la palabra nuevaPalabra. La función debe devolver la
frase con nuevaPalabra reemplazando la palabra ya existente en la frase.

Pruebas de verificación:
reemplazar ("Hola Anto", "Anto", "Ana") =>
    => "Hola Ana María"
reemplazar ("Tengo 50 años", "50", "52") => "Tengo 52 años"
'''

def reemplazar (frase, palabra, nuevaPalabra):
    listaFrase = frase.split () # Crea una lista con las palabras de la frase
    for i in range (0, len (listaFrase)): # Recorre la lista
        if listaFrase [i] == palabra: # Si la palabra es igual a la palabra a reemplazar
            listaFrase [i] = nuevaPalabra # Reemplaza la palabra
    newFrase = " ".join(listaFrase) # Une la lista en una frase con un espacio entre cada palabra
    return newFrase

print (reemplazar ("Hola Anto", "Anto", "Ana"))