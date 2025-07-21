"""
#1. Simulación de Votación con validación cruzada

name= input("Ingrese su nombre completo:")
name_conteo= len(name)
dpi= input("Ingrese su número de DPI:")
dpi=len(dpi)
departamento= input("Ingrese nombre de departamento:").lower()
año_nacimiento = int(input("Ingrese año de nacimiento:"))
edad_año=  2025 - año_nacimiento
excepcion_departamento= ["Peten", "Alta verapaz"]

if edad_año < 18 and not (departamento in excepcion_departamento and edad_año ==17):
    print("No cumple con edad requerida. No puede votar")

elif name_conteo <5:
    print("Su nombre debe poseer mas de 5 letras")

elif (dpi > 13) or (dpi < 13):
    print("DPI invalido, debe tener 13 dígitos exactamente.")
else:
    print(f"Bienvenido {name},su centro de votación es {departamento.capitalize()}")
"""

""""
#Calculadora de Impuesto Progresivos y números de dependientes.

annueal_income= float(input("Ingrese el ingreso anual:"))
dependents_number= int(input("Ingrese número de dependientes:"))
dependents_deduction= 1000 * dependents_number
deducted_income= annueal_income - dependents_deduction


if annueal_income < 40000 and dependents_number > 2:
    percentage= 0

else:
    if deducted_income <=30000:
        percentage= (deducted_income*5)/100
    elif deducted_income <=60000:
        percentage= (deducted_income*10)/100
    elif deducted_income <=100000:
        percentage= (deducted_income*15)/100
    elif deducted_income > 100000:
        percentage= (deducted_income *20)/100
total_income= annueal_income - percentage
print(f"Su ingreso anual es de:{annueal_income} \n Monto dedudido por dependientes {dependents_deduction}")
print(f"Ingreso despues de deducciones:{deducted_income}")
print(f"Ingreso despues de impuestos: {total_income} \n Impuesto total a pagar:{percentage}")
"""
"""
#Sistema de autenticación avanzado con penalización

user_and_password= [
    ["usuario1","perrito123"],
    ["usuario2","osito123"],
    ["usuario3","dinosaurio1"]
]
attempts= 0

while attempts < 3:
    user= input("Ingrese nombre de usuario:")
    password= input("Ingrese contraseña:")

    for acces in user_and_password:
        if user == acces[0] and password== acces[1]:
            print("Acceso concedido!")
            print("MENÚ \n 1. Ver perfil.\n 2. Cambiar contraseña. \n 3.Cerrar sesión")
            break
    else:
        print("Verifique usuario o contraseña...")
        attempts = attempts +1
if attempts >=3:
    print("ACCESO BLOQUEADO")

"""
"""
#4. Simulacion de Facturación de IVA, descuentos y propina

amount_products= int(input("Ingrese cantidad de productos:"))
add_prices= 0

for product in range(amount_products):
    price= int(input(f"Ingrese percio de producto no.{product + 1}:"))
    add_prices = add_prices + price

tip= input("¿Desea dejar propina? (si/no)").lower()
if tip =="si":
    amount= int(input("Ingrese cuanto desea dejar de propina (en %):"))
    amount_tip= (add_prices * amount)/100
else:
    amount_tip= 0

frequent_customer= input("¿Tiene tarjeta de cliente frecuente? (si/no):").lower()

if frequent_customer=="si":
    discount=(add_prices *10)/100
else:
    discount= 0

iva= (add_prices*12)/100
total= add_prices + iva + amount_tip - discount

print("---TOTAL DETALLADO---")
print(f"Subtotal:{add_prices}")
print(f"IVA:{iva}")
print(f"propina:{amount_tip}")
print(f"Decuento:{discount}")
print(f"Total:{total}")
"""
"""
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

"""
"""
#6.Clasificador de envios con multiples condiciones

package_weight= float(input("Ingre peso del paquete en kg:"))
distance= int(input("Ingrese distancia en km:"))
urgency= input("Es una urgencia? si/no:").lower()
package_size= input("Ingrese tamaño de paquete (grande/mediano/pequeño):").lower()

cost_weight= package_weight * 5 #5 q por kg
cost_distance= 2 * distance #1 q por k
cost_base= cost_weight + cost_distance

if urgency == "si":
     surcharge = 50
else:
     surcharge = 0

if urgency =="no" and package_weight < 5:
     discount= (cost_base -20)
else:
     discount= 0

if package_size == "grande":
    surcharge_size = 30
else:
    surcharge_size= 0

cost_total= cost_base + surcharge + discount + surcharge_size

print("---COSTO DE ENVIO---")
print(f"costo por distancia: {cost_distance}")
print(f"costo por peso:{cost_weight}")
print(f"costo base ( depende distancia y peso):{cost_base}")
print(f"Recargo por tamaño( si es grande):{surcharge_size}\n Recargo por urgencia: {surcharge}")
print(f"Descuento: {discount}\ncosto total:{cost_total}")
"""

"""

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

"""
"""
#8.Calculadora de rumboo entre puntos cardinales

coordinate1= input("Ingrese coordenada 1 (norte/sur/oeste/este):").lower()
coordinate2= input("Ingrese coordenada 2 (norte/sur/oeste/este):").lower()
coordinates= ["norte","sur","oeste","este"]

if coordinate1 in coordinates and coordinate2 in coordinates:
    True
else:
    print("Coordenada no valida")

if coordinate1 == coordinate2:
    print(f"no debes de moverte, ya te encuentras en {coordinate1}")
else:
    if coordinate1 == "norte":
        if coordinate2=="este":
            print("Debes ir hacia el Noreste")
        elif coordinate2 =="sur":
            print("Debes moverte recto hacia el sur")
        elif coordinate2== "oeste":
            print("Debes ir hacia el Noroeste")
    elif coordinate1 =="sur":
        if coordinate2=="este":
            print("Debes ir hacia el Sureste")
        elif coordinate2=="oeste":
            print("Debes ir hacia el Suroeste")
        elif coordinate2=="norte":
            print("Debes moverte recto hacia el norte")
    elif coordinate1== "oeste":
        if coordinate2=="este":
            print("Debes moverte recto hacia el este")
        elif coordinate2=="sur":
            print("Debes moverte hacia al suroeste")
        elif coordinate2=="norte":
            print("Debes moverte hacia el noreste")
    elif coordinate1=="este":
        if coordinate2=="norte":
            print("Debes moverte hacia el noreste")
        elif coordinate2=="sur":
            print("Debes moverte hacia el sureste")
        elif coordinate2=="oeste":
            print("Debes moverte recto hacia el oeste")
"""
"""
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
"""


#10. Comparador de fechas ( tipo calendario digital )

date1= input("Ingrese fecha no.1 (dia/mes/año):")
date1= date1.split("/")

date2= input("Ingrese fecha no.2 (dia/mes/año):")
date2= date2.split("/")

day1= int(date1[0])
month1= int(date1[1])
year1=int(date1[2])

day2=int(date2[0])
month2=int(date2[1])
year2=int(date2[2])

month_31= [1,3,5,7,8,10,12] #Estos meses tienen 32 días :D
month_30 = [4,6,9,11] #estos 30

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
