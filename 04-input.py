#Además de expulsar valores, datos o información, los programas reciben valores que de alguna forma manipulan y trasforman. Python tare una función incorporada llamada input, que permite ingresar datos o valores al programa.
print("Hola dime cúal es tu nombre")
name = input()
print(f"Hola " +name)
print("¿Cuantos años tienes?")
#Una característica de la función input es que solo entrega texto.
age = int(input())
print(type(age))
print("Naciste en",2023-age, sep=': ')
