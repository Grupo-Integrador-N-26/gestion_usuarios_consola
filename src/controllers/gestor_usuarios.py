from models.usuario import Usuario

def registrar_usuario_estandar():
    print("\n Registro de Usuario Estándar")
    username = input("Ingrese nombre de usuario: ")
    password = input("Ingrese contraseña: ")
    nuevo_usuario = Usuario(username, password, rol_id=2)
    nuevo_usuario.registrar()

def registrar_administrador():
    print("\n Registro de Administrador")
    username = input("Ingrese nombre de administrador: ")
    password = input("Ingrese contraseña: ")
    nuevo_admin = Usuario(username, password, rol_id=1)
    nuevo_admin.registrar()

def eliminar_usuario():
    print("\n Eliminar Usuario")
    username = input("Ingrese el nombre de usuario a eliminar: ")
    usuario = Usuario(username, password="", rol_id=0)  # No es necesario validar contraseña aquí
    usuario.eliminar()
