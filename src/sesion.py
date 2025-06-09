class Sesion:
    def __init__(self, usuario):
        self.usuario = usuario

    def es_admin(self):
        return self.usuario.perfil.nombre == "admin"

    def mostrar_menu(self):
        if self.es_admin():
            print("\nMenú Administrador:")
            print("1. Listar usuarios")
            print("2. Cambiar rol de usuario")
            print("3. Eliminar usuario")
            print("4. Salir")
        else:
            print("\nMenú Usuario Estándar:")
            print("1. Ver mis datos")
            print("2. Salir")