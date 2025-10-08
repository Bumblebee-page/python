import random

fecha = input("Introduce la fecha de tu nacimiento en formato dia/mes/año: ")
dia = fecha[: fecha.find("/")]
mesaño = fecha[fecha.find("/")+1:]
mes = mesaño[:mesaño.find("/")]
año = mesaño[mesaño.find("/")+1:]
print("Dia", dia)
print("Mes", mes)
print("Año", año)