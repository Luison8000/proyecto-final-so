import os
import psutil
import subprocess
import signal


def listar_procesos():
    print("\nPID\tNombre\t\tCPU%\tMemoria%")
    print("-" * 50)
    for proceso in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pid = proceso.info['pid']
            nombre = proceso.info['name']
            cpu = proceso.info['cpu_percent']
            memoria = proceso.info['memory_percent']
            print(f"{pid}\t{nombre[:15]}\t{cpu}\t{memoria:.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def iniciar_proceso():
    comando = input("Ingresa el comando a ejecutar (ej: firefox o sleep 60): ")
    try:
        proceso = subprocess.Popen(comando.split())
        print(f"Proceso iniciado con PID {proceso.pid}")
    except Exception as e:
        print(f"Error al iniciar proceso: {e}")


def detener_proceso():
    try:
        pid = int(input("Ingresa el PID del proceso a detener: "))
        os.kill(pid, signal.SIGTERM)
        print("Proceso detenido correctamente.")
    except Exception as e:
        print(f"Error al detener proceso: {e}")


def estado_sistema():
    cpu_total = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    print("\nEstado del Sistema")
    print("-" * 30)
    print(f"Uso de CPU: {cpu_total}%")
    print(f"Memoria usada: {memoria.percent}%")
    print(f"Memoria disponible: {memoria.available / (1024**3):.2f} GB")


def mostrar_menu():
    print("\n--- SERVIDOR DE PROCESOS ---")
    print("1. Listar procesos")
    print("2. Iniciar proceso")
    print("3. Detener proceso")
    print("4. Ver estado del sistema")
    print("5. Salir")


def main():
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listar_procesos()
        elif opcion == "2":
            iniciar_proceso()
        elif opcion == "3":
            detener_proceso()
        elif opcion == "4":
            estado_sistema()
        elif opcion == "5":
            print("Saliendo del servidor...")
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
