import random

inversion = float(input("Introduce la invercion inicial "))
interes = 0.04
balance1 = inversion *(1 + interes)
print("balance tras el primer año: " + str(round(balance1, 2)))
balance2 = balance1 *(1+ interes)
print("balance tras el segundo año: " + str(round(balance2, 2)))
balance3 = balance2 *(1+ interes)
print("balance tras el tercer año: " + str(round(balance3, 2)))