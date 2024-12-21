'''
### CALCULAR EL NÚMERO DE VALORES DE UN DICCIONARIO ###
Escriba una función numValoresDicc(d) que tome un diccionario d como
parámetro y devuelva el número de valores contenidos en las listas
asociadas a las claves.
Nota: A efectos de este ejercicio, consideramos que todos los valaores
asociados a las claves están en forma de listas.

Pruebas de verificación:
numValoresDicc ({"a":[1, 2, 3], "b":[3, "p"],"c": [8]}) => 6
numValoresDicc ({"Julie":[12, 60.1], "Fred":[26, 75.6], "David":[]}) => 4
'''

def numValoresDicc (d):
    contador = 0
    list_claves = d.keys() # Retorna una lista con las claves del diccionario
    for i in list_claves: # Recorremos las claves
        contador += len (d[i]) # Sumamos la longitud de cada lista asociada a cada clave
    return contador


d1 = {"a":[1, 2, 3], "b":[3, "p"],"c": [8]}
d2 = {"Julie":[12, 60.1], "Fred":[26, 75.6], "David":[]}
print (numValoresDicc (d1))
print (numValoresDicc (d2))
