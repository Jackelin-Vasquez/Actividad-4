#2.Calculadora de Impuesto Progresivos y números de dependientes.

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