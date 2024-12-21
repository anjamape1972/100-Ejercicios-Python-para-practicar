'''
### DIVISORES Y MÚLTIPLOS ###
Escribir una función llamada divisoresMult(n, a, numUmbral) que
permita encontrar los números (desde 0 hasta un numUmbral dado) que
son divisibles por n y que no son múltiplos de a.

Pruebas de verificación:
divisoresMult (5, 2, 100) => [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
divisoresMult (11, 3, 85) => [11, 22, 44, 55, 77]
'''

def divisoresMult (n, a, numUmbral):
    resultado = []
    for i in range (numUmbral + 1): # Se suma 1 para que el rango incluya el número numUmbral
        if i % n == 0 and i % a != 0: # Si el número es divisible por n y no es múltiplo de a
            resultado.append (i) # Se añade a la lista
    return resultado

numUmbral = int (input ("Indique hasta que número quiere trabajar: ")) # Se solicita el número hasta el que se quiere trabajar
n = int (input ("Indique el número por el que debe ser divisible: ")) # Se solicita el número por el que debe ser divisible
a = int (input ("Indique el número del que no debe ser multiplo: ")) # Se solicita el número del que no debe ser múltiplo
print (divisoresMult (n, a, numUmbral))