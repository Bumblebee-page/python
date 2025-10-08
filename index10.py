import random

barras = int(input("introduce el numero de barras vendidas que no son frescas: "))
precio = 3.49
descuento = 0.006
costo = barras * precio * (1 - descuento)
print("El costo de una barra fresca es " + str(precio) + ("$"))
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + ("%"))
print("El costo final a pagar es " + str(round(costo, 2)) + "$")