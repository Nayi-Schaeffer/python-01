#Clacular el promedio de los números en el arreglo numbers

notas = [1,2,3,4,5,6,7,8,9,10]
total = 0
for nota in notas:
    total += nota

print(f"El promedio es: {total/len(notas)}")