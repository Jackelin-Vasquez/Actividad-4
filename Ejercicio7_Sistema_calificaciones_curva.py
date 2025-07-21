#7. Sistema de calificaciones con curva
students=[]
averages=[]

for student in range(1,6):
    student_name= input(f"Ingrese nombre de estudiante {student}:")
    note1= int(input("Ingrese nota 1:"))
    note2 = int(input("Ingrese nota 2:"))
    note3 = int(input("Ingrese nota 3:"))
    students.append([student_name,note1,note2,note3])

    average= (note1 + note2 + note3)/3
    averages.append(average)

for ave in averages:
    if ave >=70:
        print("No todos los promedios son menores a 70")
    else:
        print("Todos los promedios son menores a 70")

        # Sin completar, faltaria sumar los 5 pts y volver a sacar promedios