'''
### AÑADIR ELEMENTOS A UN DICCIONARIO ###
Escribir una función llamada añadirElementoDicc (clave, valor, d),
que toma 3 parámetros de entrada: un diccionario d, una clave y un valor
asociado. La función debe permitir agregar esta clave y valor al diccionario d.
Por último, la función debe devolver el diccionario d que contiene la nueva clave y valor.

Pruebas de verificación:
añadirElementoDicc ("baptiste", 29, {"julien": 14, "laurent": 31})
# Devuelve {"julien": 14, "laurent": 31, "baptiste": 29}
añadirElementoDicc ("peso", 65.3, {})
# Devuelve {"peso": 65.3}
'''

def añadirElementoDicc(clave, valor, d):
    d[clave] = valor # Añade la clave y el valor al diccionario d que se pasa por parámetro y lo devuelve
    return d
d1 = {"julien": 14, "laurent": 31}
d2 = {}
añadirElementoDicc("baptiste", 29, d1) # Añaade la clave "baptiste" con el valor 29 al diccionario d1
añadirElementoDicc("peso", 65.3, d2) # Añade la clave "peso" con el valor 65.3 al diccionario d2
print(d1) # Muestra el diccionario d1
print(d2) # Muestra el diccionario d2

# Solicitando datos al usuario para añadir elementos al diccionario
clave = input ("Ingrese la clave: ") # Solicita la clave
valor = input ("Ingrese el valor: ") # Solicita el valor
añadirElementoDicc(clave, valor, d1) # Añade la clave y el valor al diccionario d1
print(d1) # Muestra el diccionario d1
print(d2) # Muestra el diccionario d2