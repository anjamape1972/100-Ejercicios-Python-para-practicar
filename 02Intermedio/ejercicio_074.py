'''
Escribir una función recursiva secuenciaFibonacci(N) que tome como
parámetro un número natural N positivo y devuelva el elemento de índice N
de la sucesión de Fibonacci.

Recordatorio: estamos interesados en la sucesión de enteros definida por
F1 = 1, F2 = 1 y para cualquier número natural N, por F(N+2) = F(N+1) + F(N).

Pruebas de verificación:
secuenciaFibonacci (25) => 75025
secuenciaFibonacci (45) => 1134903170
'''

def secuenciaFibonacci (N):
    if N <= 2: # Caso base de la recursión (F1 = 1, F2 = 1)
        return 1
    return secuenciaFibonacci (N-1) + secuenciaFibonacci (N-2) # F(N+2) = F(N+1) + F(N)

print (secuenciaFibonacci (25))
print (secuenciaFibonacci (35))