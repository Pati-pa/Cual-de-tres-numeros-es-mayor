# verificar entre 3 números cual es mayor que los otros


print("----------------------------------")
print("------------MAYOR O MENOR---------")
print("----------------------------------")

#input
X = int(input("INGRESE EL VALOR 1: "))
Y = int(input("INGRESE EL VALOR 2: "))
Z = int(input("INGRESE EL VALOR 3: "))
print("-------------------------------")
print("-------------------------------")

#condicion o validacion
print("-------------------------------")
print("------------RESULTADO----------")
print("-------------------------------")
if (X>Y):
    r = X
else:
    r = Y

if (r>Z):
    print("El numero " + str(r) + " es el numero mayor de todos")
else:
    print("El numero " + str(Z) + " es el numero mayor de todos")

