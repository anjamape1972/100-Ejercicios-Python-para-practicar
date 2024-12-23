'''
### NÚMERO DE DÍAS Y HORAS ###
Escribir una función numDiasHoras(fechaInicio, fechaFin) que tome dos
parámetros de entrada: la fecha de inicio fechaInicio y la fecha de fin
fechaFin. Esta función nos permitirá calcular el número de días y el
número de horas entre la fecha de inicio y la fecha de fin pasadas como
parámetros. La función debe devolver la tupla (NumDias, NumHoras).

Pruebas de verificación:
numDiasHoras ("2022/05/15", "2022/06/20") => (36, 864)
numDiasHoras ("2022/04/01", "2022/04/27") => (26, 624)
'''

from datetime import datetime # Importamos la librería datetime

def numDiasHoras (fechaInicio, fechaFin):
    formato = "%Y/%m/%d" # Formato de fecha a utilizar
    fecha1 = datetime.strptime (fechaInicio, formato) # Convertimos la fechaInicio a formato datetime
    fecha2 = datetime.strptime (fechaFin, formato) # Convertimos la fechaFin a formato datetime
    diferencia = fecha2 - fecha1 # Restamos las fechas para obtener la diferencia de días y horas
    dias = diferencia.days # Obtenemos los días de la diferencia de fechas
    horas = diferencia.total_seconds () // 3600 # Obtenemos las horas de la diferencia de fechas
    return (int (dias), int (horas)) # Retornamos la tupla con los días y horas en formato entero

print (numDiasHoras ("2022/05/15", "2022/06/20"))
print (numDiasHoras ("2022/04/01", "2022/04/27"))