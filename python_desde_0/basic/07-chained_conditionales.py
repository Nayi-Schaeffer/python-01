#Podemos encontrar situaciones donde se requiere de más de una expresión boolenana para determinar el flujo de ejecución ddl programa.

first_number = int(input("Dame el primer número"))
second_number = int(input("Dale el segundo número"))

if first_number < second_number:
    print("El segundo es mayor")
elif first_number > second_number:
    print("El primero es mayor")
else:
    print("Son iguales")
    