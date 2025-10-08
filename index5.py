import random
peso = input("ingrese su peso en kg ")
estatura = input("Ingrese su estatura en metros ")
imc = round(float(peso)/float(estatura)**2,2)
print("tu indice de masa corporal es " + str(imc))