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
