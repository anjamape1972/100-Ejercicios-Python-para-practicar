'''
### INVERTIR EL ORDEN DE LAS PALABRAS ###
Escribir una función invertirFrase(frase) que toma una frase como
parámetro e invierte el orden de las palabras en la frase. La función debe
devolver la frase con las palabras invertidas.

Pruebas de verificación:
invertirFrase ("Hola a todo el mundo") => mundo el todo a Hola
invertir frase ("Manzana") => Manzana
'''

def invertirFrase (frase):
    listFrase = frase.split () # Convertir la frase en una lista de palabras
    newListFrase = [] # Lista vacía para guardar las palabras invertidas
    for i in listFrase: # Recorrer la lista de palabras
        newListFrase.insert(0, i) # Insertar la palabra en la primera posición
    newFrase = " ".join (newListFrase) # Convertir la lista de palabras en una frase
    return newFrase

frase1 = "Hola a todo el mundo"
frase2 = "Manzana"
frase3 = "Don Quijote de la Mancha"
print (invertirFrase (frase1))
print (invertirFrase (frase2))
print (invertirFrase (frase3))