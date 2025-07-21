#10. Comparador de fechas ( tipo calendario digital )

date_1= input("Ingrese fecha no.1 (dia/mes/año):")
date1= date_1.split("/")

date_2= input("Ingrese fecha no.2 (dia/mes/año):")
date2= date_2.split("/")

day1= int(date1[0])
month1= int(date1[1])
year1=int(date1[2])

day2=int(date2[0])
month2=int(date2[1])
year2=int(date2[2])

month_31= [1,3,5,7,8,10,12] #Estos meses tienen 32 días :D
month_30 = [4,6,9,11] #estos 30

if (month1 <1 or month2 >12) or (month2 < 1 or month2 > 12):
    print("Mes no valido")
else:
    if month1 in month_31 or month2 in month_31:
        if (day1 < 1 or day1 >31) or (day2 <1 or day2 >31):
            print("Día no valido")
    elif month1 in month_30 or month2 in month_30:
        if (day1 < 1 or day1 > 30) or (day2 <1 or day2 >30):
            print("Día no valido")
    else:
        if month1 ==2 or month2 ==2:
            leap_year1 = (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0)
            leap_year2 = (year2 % 4 == 0 and year2 % 100 != 0) or (year2 % 400 == 0)

            if month1 == 2:
                if leap_year1:
                    if day1 < 1 or day1 > 29:
                        print("Fecha 1 no válida")
                else:
                    if day1 < 1 or day1 > 28:
                        print("Fecha 1 no válida")

            if month2 == 2:
                if leap_year2:
                    if day2 < 1 or day2 > 29:
                        print("Fecha 2 no válida")
                else:
                    if day2 < 1 or day2 > 28:
                        print("Fecha 2 no válida")

if year1 > year2:
    print(f"La fecha {date_1} es mayor que la fecha {date_2}")
    print("No estan en el mismo año")
elif year1 < year2:
    print(f"la fecha {date_2} es mayor que la fecha {date_1}")
    print("No estan en el mismo año")
else:
    if year1 == year2:
        print("Estan en el mismo año")
    elif month1 > month2:
        print(f"la fecha {date_1} es mayor que la fecha {date_2}")
    elif month1 < month2:
        print(f"La fecha {date_2} es mayor que la fecha {date_1}")
    else:
        if day1 > day2:
            print(f"la fecha {date_1} es mayor qe la fecha {date_2}")
        elif day1 < day2:
            print(f"La fecha {date_2} es mayor que la fecha {date_1}")
        else:
            print("Las fechas son iguales")

if month1 == month2:
    print("Estan en el mismo mes")
else:
    print("No estan el mismo mes")

total_day_1 = 0
for y in range(year1):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        total_day_1 = total_day_1 + 366
    else:
        total_day_1 = total_day_1 + 365
month = 1
while month < month1:
    if month == 2:
        if (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0):
            total_day_1 =total_day_1+ 29
        else:
            total_day_1 = total_day_1 +28
    elif month in month_30:
        total_day_1 = total_day_1+ 30
    else:
        total_day_1 =total_day_1+ 31
    month = month + 1

total_day_1 = total_day_1+ day1




total_day_2 = 0
for y in range(year2):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        total_day_2 = total_day_2 + 366
    else:
        total_day_2 = total_day_2 + 365
month = 1
while month < month2:
    if month == 2:
        if (year2 % 4 == 0 and year2 % 100 != 0) or (year2 % 400 == 0):
            total_day_2 =total_day_2+ 29
        else:
            total_day_2 = total_day_2 +28
    elif month in month_30:
        total_day_2 = total_day_2+ 30
    else:
        total_day_2 =total_day_2+ 31
    month = month + 1

total_day_2 = total_day_2+ day2

diference= total_day_1 - total_day_2
print(f"Entre la fecha {date_1} y la fecha {date_2} han pasado {diference} día/s")