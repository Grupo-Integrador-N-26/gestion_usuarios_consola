from usuario import Usuario
from rol import Rol
from permiso import Permiso
from sesion import Sesion

usuarios = []
roles = []

def inicializar_roles():
    admin = Rol("admin")
    admin.agregar_permiso(Permiso("listar_usuarios"))
    admin.agregar_permiso(Permiso("cambiar_rol"))
    admin.agregar_permiso(Permiso("eliminar_usuario"))

    estandar = Rol("estandar")
    estandar.agregar_permiso(Permiso("ver_datos"))

    roles.append(admin)
    roles.append(estandar)

def obtener_rol_por_nombre(nombre):
    for rol in roles:
        if rol.nombre == nombre:
            return rol
    return None

def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    nombre = input("Nombre de usuario: ").strip()
    contraseña = input("Contraseña (mínimo 6 caracteres, con letras y números): ").strip()

    print("Elegí un rol para el usuario: ")
    print("1. Admin")
    print("2. Estándar")
    rol_opcion = input("Rol (1 o 2): ").strip()

    if rol_opcion == "1":
        rol = obtener_rol_por_nombre("admin")
    elif rol_opcion == "2":
        rol = obtener_rol_por_nombre("estandar")
    else:
        print("Opción inválida. Registro cancelado")
        return
    
    nuevo_usuario = Usuario(nombre, contraseña,rol)

    if not nuevo_usuario.es_contraseña_valida():
        print(" Contraseña inválida. Debe tener mínimo 6 caracteres, con letras y números.")
        return

    usuarios.append(nuevo_usuario)
    print(f"Usuario {nombre} registrado exitosamente con rol {rol.nombre}")

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    nombre = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    for user in usuarios:
        if user.nombre_usuario == nombre and user.contraseña == contraseña:
            print(" Inicio de sesión exitoso.")
            return Sesion(user)
    print(" Credenciales inválidas.")
    return None

def ejecutar_menu_admin():
    global usuarios
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Listar usuarios")
        print("2. Cambiar rol de un usuario")
        print("3. Eliminar usuario")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nUsuarios registrados:")
            for u in usuarios:
                print(f"- {u.nombre_usuario} ({u.perfil.nombre})")

        elif opcion == "2":
            nombre = input("Nombre de usuario a modificar: ")
            nuevo_rol = input("Nuevo rol (admin/estandar): ")
            user = next((u for u in usuarios if u.nombre_usuario == nombre), None)
            if user and nuevo_rol in ["admin", "estandar"]:
                user.perfil = obtener_rol_por_nombre(nuevo_rol)
                print(" Rol actualizado.")
            else:
                print(" Usuario o rol inválido.")

        elif opcion == "3":
            nombre = input("Nombre de usuario a eliminar: ")
            global usuario
            usuarios = [u for u in usuarios if u.nombre_usuario != nombre]
            print(" Usuario eliminado (si existía).")

        elif opcion == "4":
            break
        else:
            print(" Opción inválida.")

def ejecutar_menu_usuario(usuario):
    while True:
        print("\n--- Menú Usuario Estándar ---")
        print("1. Ver mis datos")
        print("2. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(f"Usuario: {usuario.nombre_usuario}")
            print(f"Rol: {usuario.perfil.nombre}")
        elif opcion == "2":
            print("Se cerró sesión")
            break
        else:
            print(" Opción inválida.")

def main():
    inicializar_roles()
    while True:
        print("\n--- Sistema de Gestión de Usuarios ---")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            sesion = iniciar_sesion()
            if sesion:
                if sesion.es_admin():
                    ejecutar_menu_admin()
                else:
                    ejecutar_menu_usuario(sesion.usuario)
        elif opcion == "3":
            print(" Saliendo del programa.")
            break
        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    main()
