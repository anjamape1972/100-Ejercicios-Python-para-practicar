'''
### SOLICITAR UNA LISTA AL USUARIO ###
Escribir un programa que permita pedir una lista de enteros al usuario desde la
consola. El programa deberá preguntar el número de elementos que debe contener
la lista. El programa debe almacenar esta lista en una variable llamada
lista_usuario y mostrarla al final del programa.
'''

lista_usuario = []

try: # Se solicita al usuario que introduzca el número de elementos que contendrá la lista.
    elementsNumber = int (input ("Indique cuántos elementos contendrá la lista: "))
    for i in range (elementsNumber): # Recorremos la lista y solicitamos al usuario que introduzca los elementos.
        try:
            elementsNumber = int (input ("Escriba un número: "))
            lista_usuario.append (elementsNumber) # Añadimos los elementos a la lista.
        except ValueError: # Si el usuario introduce un valor que no es numérico, se muestra un mensaje de error.
            print (f"El valor introducido debe ser de tipo numérico.")
except ValueError: # Si el usuario introduce un valor que no es numérico, se muestra un mensaje de error.
    print ("Debe introducir un valor de tipo numérico.")

print (f"La lista generada por el usuario es la siguiente: {lista_usuario}.")