# Imprimir un programa que imprima una lista de los estudiantes con promedio superior a 6

averages = {
    "Seba": 5,
    "Gaby": 6.5,
    "Fran": 7,
    "Jose": 6.4,
    "Coni": 6.2,
    "Gonza": 4.8
}

approved_student = []

for student in averages.keys():# => ["seba", "Gaby", "Fran", etc]
    if averages[student]  >6:
        approved_student.append(student)

print(approved_student)
