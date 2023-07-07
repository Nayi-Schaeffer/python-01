#Una evaluación condicional puede estar dentro de otra, ej:

name = input("Cual es tu nombre")
age = int(input("Dime tu edad"))

print(f"hola{name}!")

if age >= 18:
    drink = input("¿Qué quieres cerveza o vino?")
    if(drink) == "Cerveza":
        print("Aqui tienes tu cerveza")
    else:
        print("Aca esta tu vino")
else:
    juice = input("Quieres jugo de frutilla o naranja?")
    if(juice == "frutilla" or juice == "frutillas"):
        print("Aca tienes tu jugo de fresas")
    else:
        print("Toma tu jugo de naranja")