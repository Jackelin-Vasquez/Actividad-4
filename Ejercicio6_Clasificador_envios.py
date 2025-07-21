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