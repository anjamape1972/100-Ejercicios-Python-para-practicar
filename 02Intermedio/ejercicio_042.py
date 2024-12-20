'''
### CREACIÓN DE MOTIVOS ###
Escribe un programa que muestre la siguiente pirámide de estrellas:

*
**
****
******
********
**********

'''

print ("*") # Imprime una línea con un solo asterisco para que la pirámide tenga una base impar
for i in range (2, 11, 2):
    print (i*"*", end="") # end="" para que no haga salto de línea al final de cada print
    print ()

# Otra forma de hacerlo
for i in range (1, 12): # 12 para que llegue hasta 10 y no 11 como en el rango anterior
    if i % 2 == 0 or i == 1: # Si es par o es 1 imprime la cantidad de asteriscos correspondiente
        print (i*"*") 