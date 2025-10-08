import random
peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el numero de payasos a enviar: "))
muñecas = int(input("Introduce el numero de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))