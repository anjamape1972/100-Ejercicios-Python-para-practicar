'''
Escriba un programa que permita calcular el tiempo de ejecución
de un scrpit. Tomemos como ejemploel scrpit del ejercicio 24
y calculemos el tiempo de ejecución.
El programa debe mostrar al final la tabla de multiplicación
del ejercicio 24 junto con el tiempo de ejecución.
'''

import time

number = int (input ("Indique de qué número quiere ver la tabla: "))

for i in range (11):
    result = number * i
    print (f"{number} x {i} = {result}")

start = time.time()
end = time.time()
print(f"El tiempo de ejecución del script es de {end - start} segundos.")
