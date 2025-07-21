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