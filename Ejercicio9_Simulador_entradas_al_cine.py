#9. Simulador de entradas al cine con validación multiple

age= int(input("Ingrese su edad:"))
day_week = input("Ingrese día de la semana:").lower()
student= input("¿es estudiante:").lower()
week= ["Lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
if day_week in week:
    week= True
else:
    print("Día inexistente")

if age < 13:
    print("No puede ver peliculas para mayores de 15 años")
else:
    print("Puede entrar a peliculas para mayores de 15 años :D")
    if day_week == "miercoles":
        price= 50
    if student == "si":
        price= 35
    else:
        price= 50

    print(f"El precio de su entrada es:{price}")