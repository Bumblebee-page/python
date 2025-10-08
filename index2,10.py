import random

producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el numero de unidades: "))
print("{producto}: {unidades:3d} unidades x {precio:09.2f}$ = {total:011.2f}$".format(producto = producto, unidades = unidades, precio= precio, total = unidades * precio))
