# Escribir un programa que cuente las letras de una palabra en un diccionario.

user_option = input("Ingresa una palabra\n")

dic = {}

for letter in user_option:
    if letter in dic:
        dic[letter] += 1
    else:
        dic[letter] = 1

print(dic)