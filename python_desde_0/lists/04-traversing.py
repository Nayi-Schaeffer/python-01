#la forma más común de recorrer una lista es utilizando el loop for.

some_list = ["code", "terminal", "linux", "git"]

for elem in some_list:
    print(elem)

#Lo anterior funciona bien si solo queremos utilizar los valores que ya existen. pero si necesitamos actualizar algún valor necesitaremos los índices 

numbers = [1,2,3,4,5,6,7,8,9,10]

for index in range(len(numbers)):
    numbers[index] = numbers[index] *2
print(numbers)