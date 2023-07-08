notas = [40,40,50,70,70,70]
total = 0
for nota in notas:
    total += nota

print(f"El promedio es: {total/len(notas)}")