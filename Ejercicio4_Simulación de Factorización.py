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