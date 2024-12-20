'''
Escribir un programa que permita sumar los valores del siguiente
diccionario:
{"Manzana": 15, "Banana": 8, "Fresa": 12, "Kiwi": 9, "Melocotón": 2}
'''

frutas = {"Manzana": 15, "Banana": 8, "Fresa": 12, "Kiwi": 9, "Melocotón": 2}

suma = 0
for fruta in frutas:
    suma += frutas[fruta]

print(suma)