'''
### FILTRADO DE PALABRAS POR LONGITUD ###
Escribir una función llamada filtrarPalabras(frase, longitudMinima) que
tome como parámetros una frase y filtre las palabras con una longitud
estrictamente menor que el parámetro longitudMinima. La función debe
devolver la misma frase sin las palabras filtradas.

Nota: se considera que las palabras en una frase están separadas por
espacios.

Pruebas de verificación:
filtrarPalabras ("Hola a todos", 4) => Hola todos
filtrarPalabras ("¿Cuál es tu origen?", 3) => ¿Cuál origen?
'''

def filtrarPalabras (frase, longitudMinima):
    listFrase = frase.split() # Convierte la frase en una lista de palabras
    newFraseList = [] # Lista vacía para almacenar las palabras filtradas
    for palabra in listFrase: # Recorre la lista de palabras de la frase
        if len (palabra) >= longitudMinima: # Si la longitud de la palabra es mayor o igual a la longitud mínima
            newFraseList.append (palabra) # Agrega la palabra a la lista de palabras filtradas
    newFraseList = " ".join (newFraseList) # Convierte la lista de palabras filtradas en una cadena
    return newFraseList

print (filtrarPalabras ("Hola a todos", 4))
print (filtrarPalabras ("¿Cuál es tu origen?", 3))