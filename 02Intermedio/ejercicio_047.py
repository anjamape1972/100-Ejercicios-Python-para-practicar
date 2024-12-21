'''
### CONTROL DE MAYÚSCULAS ###
Escriba una función ControlMay(frase) que tome una frase como parámetro
y compruebe si dicha frase contiene al menos una letra mayúscula. Si es así,
la función debe devolver True, en caso contrario False.

Pruebas de verificación:
ControlMay ("Las verduras son buenas para la salud") => True
ControlMay ("estoy aprendiendo el lenguaje python") => False
'''

def ControlMay (frase):
    for i in frase: # Recorremos la frase
        if i.isupper(): # Si el caracter es mayúscula devolvemos True
            return True
        else:
            return False

print (ControlMay ("Las verduras son buenas para la salud"))
print (ControlMay ("estoy aprendiendo el lenguaje python"))