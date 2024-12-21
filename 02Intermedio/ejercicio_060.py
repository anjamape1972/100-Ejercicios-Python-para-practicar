'''
### CÁLCULO DEL MÁXIMO COMÚN DIVISOR ###
Escribir una función calculoMCD(a, b) que tome como parámetros dos enteros
a y b y calcule el máximo común divisor utilizando el algoritmo de Euclides.

Recordatorio: La división euclidiana de a por b se escribe como sigue:
    a = b * q + r, donde q es el cociente y r es el resto de la división.

Pruebas de verificación:
calculoMCD (3, 5) => 1
calculoMCD (5, 15) => 5
'''

def calculoMCD (a, b):
    divisoresA = [] # Lista para guardar los divisores de a
    divisoresB = [] # Lista para guardar los divisores de b
    divisoresAyB = [] # Lista para guardar los divisores comunes de a y b
    if (a > 0 and b > 0): # Verificamos que los dos valores sean positivos
        for i in range (1, a + 1): # Calculamos los divisores de a
            if a % i == 0: # Si el residuo de la división de a entre i es 0, entonces i es divisor de a
                divisoresA.append (i) # Agregamos i a la lista de divisores de a
        for j in range (1, b + 1): # Calculamos los divisores de b
            if b % j == 0: # Si el residuo de la división de b entre j es 0, entonces j es divisor de b
                divisoresB.append (j) # Agregamos j a la lista de divisores de b
        for divA in divisoresA: # Recorremos la lista de divisores de a
            for divB in divisoresB: # Recorremos la lista de divisores de b
                if divA == divB: # Si el divisor de a es igual al divisor de b
                    divisoresAyB.append (divA) # Agregamos el divisor a la lista de divisores comunes
        return max (divisoresAyB) # Retornamos el máximo valor de la lista de divisores comunes
    else: # Si alguno de los valores es negativo
        return "Los dos valores deben ser positivos para poder calcular el MCD."

print (calculoMCD (3, 5))
print (calculoMCD (5, 15))
print (calculoMCD (5, -1))
print (calculoMCD (5, 0))