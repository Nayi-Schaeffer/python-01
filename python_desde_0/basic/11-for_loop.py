# En python algunos tipo de valores son considerados colecciones como las listas, diccionarios, string, tuplas y sets. Estas colecciones se pueden recorrer.
# Con el "for" loop podemos ejecutar un conjunto de sentencias,una por cada elemneto de la coleción.

word = "banana"
index = 0
while index < (len(word)):
    print(word[index])
    index += 1

print("--------------")

for letter in "banana":
    print(letter)

# print(len("banana"))


#for letter in "banana":
#    print(letter)