#En esta sección conoceremos uno de los tipos de datos más utiles de python. Las listas
# Similar a los string, las listas son secuencias de valores. En los strings los valores serían las letras, mientras que en una lista los valores pueden ser cualquier tipo. Los valores de una lista se les llama elementos o items.
# La forma más directa de cerar listas es con los corchetes []. Ej:

import numbers


numbers = [10,20,30,40]
animals = ["dog", "cat", "frog"]

#El primer ejemplo es una lista de solo números y el segundo de solo strings. Los elementos pueden ser de cualquier tipo.

mixed = ["hola", 42, True, [20,40]]

#Incluso podemos tener listas dentro de listas o aninadas.

#Podemos crear una listra vacía solo con los [].

emty = []

print(numbers, animals, mixed,emty)