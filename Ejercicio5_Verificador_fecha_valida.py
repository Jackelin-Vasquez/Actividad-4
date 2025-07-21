#5.Verificador de fecha valida con día de la semana.

day= int(input("Ingrese día:"))
month= int(input("Ingrese mes en números (1-12):"))
year= int(input("Ingrese año:"))

month_31= [1,3,5,7,8,10,12] #Estos meses tienen 32 días :D
month_30 = [4,6,9,11] #estos 30
days_week= ["Sabado","Domingo","Lunes","Martes","Miercoles","Jueves","Viernes"]


if month < 1 or month >12:
    print("mes no valido!")

if month in month_31:
    if day >31:
        print("Día no valido...")

elif month in month_30:
    if day >30:
        print("Día no valido...")

elif month==2:
    leap_year= (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if leap_year:
        if day < 1 or day >29:
            print("Fecha no valida....")
    else:
        if day < 1 or day > 28:
            print("Fecha no valida...")
if month <3:
    month= month + 12
    year= year -1

j= year//100
k= year %100

# h = (day + (((month +1)*26)/10)+k +(k/4)+(j+4)-2*j)%7
h = (day + ((13*(month+1)//5))+k +(k//4)+(j//4)-2*j)%7

day_week= days_week[int(h)]

print(f"La fecha {day}/{month}/{year} fue un día {day_week}")