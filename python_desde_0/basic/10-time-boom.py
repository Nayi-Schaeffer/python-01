import time
#Ejercicio hacer un programa que parta contando desde 10 y que al llegar a 0 diga boom
#tip esperar un segundo en cada iteración utilizando time.sleep(1) 

num = 10

while num >= 0:
    print(num)
    num == num - 1
    time.sleep(1)

print("¡BooM!")