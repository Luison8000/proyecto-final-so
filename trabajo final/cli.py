def login():
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    respuesta = enviar_comando(f"LOGIN:{usuario}:{password}")

    if respuesta == "LOGIN_OK":
        print("Autenticación exitosa")
        return True
    else:
        print("Credenciales incorrectas")
        return False
