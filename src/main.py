from database.init_db import crear_tablas
from controllers.gestor_usuarios import (
    registrar_usuario_estandar,
    registrar_administrador,
    eliminar_usuario
)

def mostrar_menu():
    print("\n MENÚ PRINCIPAL")
    print("1. Registrar usuario estándar")
    print("2. Registrar administrador")
    print("3. Eliminar usuario")
    print("4. Salir")

def main():
    crear_tablas()
    print(" Base de datos inicializada correctamente.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario_estandar()
        elif opcion == "2":
            registrar_administrador()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            print(" Saliendo del programa.")
            break
        else:
            print(" Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

