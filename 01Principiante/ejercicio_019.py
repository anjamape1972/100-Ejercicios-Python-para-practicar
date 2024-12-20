'''
Escriba un programa que permita invertir una cadena de caracteres.
El programa debe invertir la variable ch que contiene la frase
"Hola a todos"
'''

ch = "Hola a todos"
ch_reverse = ""
for i in range (len (ch) - 1, -1, -1):
    ch_reverse += ("".join (ch[i]))

print (ch_reverse)

### Alternativa utilizando slicing ###
ch_reverse2 = ch[::-1]  # [comienzo:fin:saltos] Al poner -1 le indicamos reversa de la cadena
print(ch_reverse2)