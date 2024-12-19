'''
Crear una serie de instrucciones en Python que permitan declarar
una variable var y asignarle el valor "Hola". Luego, el programa
debe verificar si la variable var es un entero o una cadena de
caracteres. Si es un enetero, el programa debe imprimir en la consola
"Entero", y si es una cadena de caracteres, el programa imprimirá
"Cadena de caracteres" en la consola.
'''

var = "Hola"

### Utilizando la función isinstance ###
if isinstance (var, int):
    print ("Entero")
elif isinstance (var, str):
    print ("Cadena de caracteres")

### Utilizando la clase type ###
if type (var) == int:
    print ("Entero")
elif type (var) == str:
    print ("Cadena de caracteres")