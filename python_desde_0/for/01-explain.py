# 

some_text = "Hola inmundo"

#print(some_text[7])  #para sitar una letra dentro de la palabra

word_one = ""

for letter in some_text:
    if letter == " ":
        word_one += "\n"
    else:
        word_one += letter
print(word_one)


