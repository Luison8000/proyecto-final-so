def main():
    autenticado = False

    while not autenticado:
        autenticado = login()

    opcion = ""

    while opcion != "5":
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(enviar_comando("LIST"))

        elif opcion == "2":
            nombre = input("Comando a ejecutar: ")
            print(enviar_comando(f"START:{nombre}"))

        elif opcion == "3":
            pid = input("PID a detener: ")
            print(enviar_comando(f"STOP:{pid}"))

        elif opcion == "4":
            print(enviar_comando("STATUS"))

        elif opcion == "5":
            print("Saliendo...")

        else:
            print("Opción inválida.")
