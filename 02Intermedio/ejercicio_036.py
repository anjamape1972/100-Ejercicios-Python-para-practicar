'''
### CALCULAR LA SUMA DE LOS DÍGITOS DE UN NÚMERO ###
Escribe un programa que calcule la suma de los dígitos de un número.
El programa debe mostrar el resultado en la consola.
'''

number = input ("Ingrese un número: ")

# con funciones hacerlo
def suma_digitos (number):
    return sum (int (i) for i in number)

print (f"La suma de los dígitos del número {number} es: {suma_digitos (number)}")