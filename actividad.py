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

#Calculadora de Impuesto Progresivos y números de dependientes.

annueal_income= float(input("Ingrese el ingreso anual:"))
dependents_number= int(input("Ingrese número de dependientes:"))
dependents_deduction= 1000 * dependents_number

if annueal_income < 40000 and dependents_number > 2:
    percentage= 0

elif annueal_income >=0 and annueal_income <=30000:
    percentage= (annueal_income/5)*100
elif annueal_income >=30001 and annueal_income <=60000:
    percentage= (annueal_income/10)*100
elif annueal_income >= 60001 and annueal_income <=100000:
    percentage= (annueal_income/20)*100

deducted_income= annueal_income - dependents_deduction
