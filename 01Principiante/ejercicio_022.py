'''
### UTILIZACIÓN DEL MÉTODO format() ###
Escribir un programa que permita truncar un número decimal
a 2 cifras después de la coma.
Por ejemplo, si tomamos el número decimal 187.632587, el
programa deberá devolver 187.63.
'''

numero = 187.632587
print("{:.2f}".format(numero)) # Formatea a 2 decimales y lo redondea