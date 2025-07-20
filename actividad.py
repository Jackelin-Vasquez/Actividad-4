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

#5.Verificador de fecha valida con día de la semana.

day= int(input("Ingrese día:"))
month= int(input("Ingrese mes en números (1-12):"))
year= int(input("Ingrese año:"))

month_31= [1,3,5,7,8,10,12] #Estos meses tienen 32 días :D
month_30 = [4,6,9,11] #estos 30
days_weekend= ["Sabado","Domingo","Lunes","Martes","Miercoles","Jueves","Viernes"]


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

h = (day + ((13*(month +1)/5))+k +(k/4)+(j/4)-2*j)%7
day_weekend= days_weekend[int(h)]


print(f"La fecha {day}/{month}/{year} fue un día {day_weekend}")






