'''
Escribir un programa que muestre la tabla de multiplicación del
número que le indiquemos.
'''

number = int (input ("Indique de qué número quiere ver la tabla: "))

for i in range (11):
    result = number * i
    print (f"{number} x {i} = {result}")