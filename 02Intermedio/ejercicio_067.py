'''
### LA CLAVE CON EL MÁXIMO NÚMERO DE VALORES ÚNICOS ###
Escribir una función claveMaxValDicc(d) que tome como parámetro un
diccionario d y devuelva la clave que tiene el mayor número de valores
únicos.

Nota: En este ejercicio consideramos que los valores de todas las claves
están en forma de listas.

Prueba de verificación:
claveMaxValDicc ({"a":[9, 10, 9, 7, 3, 1], "b":[5, 3, 2, 2, 2], "c":[1, 1, 1, 1, 1, 1, 8, 2]}) => a
claveMaxValDicc ({"dtg":[6, 8, 1], "fgb":[2.5, "a"], "klm":["p", 3, 3]}) => dtg
'''

def claveMaxValDicc (d):
    clave = [] 
    listKeys = list (d.keys ()) # Creamos una lista con las claves del diccionario
    for key in listKeys: # Recorremos las claves
        numElementsValue = len (set (d [key])) # Obtenemos el número de elementos únicos
        clave.append ((key, numElementsValue)) # Añadimos la clave y el número de elementos únicos a la lista clave
    clave.sort (key= lambda x: x[1]) # Ordenamos la lista clave por el número de elementos únicos
    maxClave = clave [-1][0] # Obtenemos la clave con el mayor número de elementos únicos
    return maxClave

print (claveMaxValDicc ({"a":[9, 10, 9, 7, 3, 1], "b":[5, 3, 2, 2, 2], "c":[1, 1, 1, 1, 1, 1, 8, 2]}))
print (claveMaxValDicc ({"dtg":[6, 8, 1], "fgb":[2.5, "a"], "klm":["p", 3, 3]}))