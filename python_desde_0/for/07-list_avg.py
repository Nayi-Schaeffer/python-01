#Clacular el promedio de los números en el arreglo numbers

import numbers


numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0
for number in numbers:
    total += number

print(f"El promedio es: {total/len(numbers)}")