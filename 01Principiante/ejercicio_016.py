'''
Escriba las instrucciones que permitan ordenar una cadena
de caracteres en orden alfabético ascendente. Para probar,
vamos a tomar la cadena c = "francia".
El programa debe devolver "aacfinr"
'''

c = "francia"

c_asc = ("".join (sorted(c)))
print (c_asc)