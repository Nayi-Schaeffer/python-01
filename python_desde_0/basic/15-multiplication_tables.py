# EJERCICIO: Utilizando "for" y "range()", crear un algoritmo que imprima en la terminal las tblas de multiplicar del 1 al 12
# La tabla del 1 es:
print("---TABLA DEL 1---")
for table in range(1,13):
    print(f"LA TABLA DEL = {table}")
    for step in range(1,13):    
        print(f" {table} X {step}= {table*step}")