#La sintaxis para acceder a los elementos es con el nombre de la variable que tienen las listas segunda de los corchetes[] con su índice al interior

fruits = ["apple", "orange", "pineapple"]
print(fruits[0])

#Los elementos en una lista tienen una posición númerica partiendo desde el 0

#La listas son modificables, es decir, pueden mutar. En otras palabras las listas son mutables, a diferencia de los strings que son inmutables.

fruits[0] = "chocolate"

print(fruits)

#Ej: los string son inmutables, es decir una vez que se establece su valor, este no se puede modificar.

some_string = "Mundo"

print(some_string[0])

#La siguiente sentencia es un error. Los string no se pueden modificar 
#some_string [0] = "x"

print(some_string)

#Los indices de las listas se pueden reemplazar por cualquier espresión que entregue un entero que está dentro de los índices definidos 

import random

print(fruits[random.randint(0,len(fruits)-1)])







