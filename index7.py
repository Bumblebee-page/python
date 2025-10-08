import random
cantidad = float(input("cantidad a invertir "))
interes = float(input("cantidad porcentual anual "))
años = int(input("Años "))
print("Capital final: " + str(round(cantidad* (interes / 100 +1) ** años, 2)))