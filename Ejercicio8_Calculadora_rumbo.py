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