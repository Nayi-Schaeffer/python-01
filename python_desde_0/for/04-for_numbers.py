#Utilizando for y range imprimir los números del 1 al 10, uno en cada fila.

for num in range(1,11):
    row = ""
    for digit in range(1,num+1):
        row += str(digit)
    print(row)



