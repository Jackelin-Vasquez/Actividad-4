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