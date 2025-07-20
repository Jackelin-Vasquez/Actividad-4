#1. Simulación de Votación con validación cruzada

name= input("Ingrese su nombre completo:")
name_conteo= len(name)
dpi= input("Ingrese su número de DPI:")
dpiconteo=len(dpi)
departamento= input("Ingrese nombre de departamento:")
año_nacimiento = int(input("Ingrese año de nacimiento:"))

edad_año=  2025 - año_nacimiento

if edad_año < 18:
    print("No es mayor de edad. No puede votar")

if name_conteo <5:
    print("Su nombre debe poseer mas de 5 letras")

if (dpi > 13) and (dpi < 13):
    print("DPI invalido, debe tener 13 dígitos exactamente.")