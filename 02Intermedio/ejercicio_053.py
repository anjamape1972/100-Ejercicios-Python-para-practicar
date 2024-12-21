'''
### PRESENCIA DE UN A VOCAL EN UNA CADENA ###
Escribir una función llamada presenciaVocal(frase) que tome como
parámetro una frase y verifique si contiene una vocal o no. Si la frase
contiene una vocal, la función devuelve True, de lo contrario devuelve
False.

Pruebas de verificación:
presenciaVocal ("Voy a darme una ducha") => True
presenciaVocal ("rbhpm") => False
'''

def presenciaVocal (frase):
    vowels = "aeiou" # Definimos las vocales
    for i in vowels: # Iteramos sobre las vocales
        if i in frase: # Si la vocal está en la frase
            return True
        else: # Si no está
            return False

frase = input ("Escriba el texto en el que quiere ver si hay vocales: ") # Pedimos la frase
print (presenciaVocal (frase))