# Imprime una lista con todos los valores.

averages = {
    "Seba": 5,
    "Gaby": 6.5,
    "Fran": 7,
    "Jose": 6.4,
    "Coni": 6.2,
    "Gonza": 4.8
}

grades = averages.values()
vals = []
for grade in grades:
    vals.append(grade)
print(vals)