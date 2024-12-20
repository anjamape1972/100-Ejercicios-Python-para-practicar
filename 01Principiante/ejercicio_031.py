'''
### VISUALIZACIÓN DE MOTIVOS ###
Escribe un programa que muestre los siguientes números
en la consola:

5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
'''

lista = list(range(5, 21))
for i in range (8): # Con esto hacemos que se repita 8 veces la impresión de la lista
    print (*lista) # El * es para desempaquetar la lista, para que no se imprima en forma de lista

# Otra forma de hacerlo
for i in range(8):
    for j in range(5, 21):
        print(j, end=" ") # Con el end=" " hacemos que no se haga un salto de línea
    print() # Con esto hacemos que se haga un sal