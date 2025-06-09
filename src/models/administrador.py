from src.models.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, correo, contraseña):
        super().__init__(nombre, correo, contraseña)
        self.rol = "administrador"

    def eliminar_usuario(self, usuario):
        """Simula la eliminación de un usuario"""
        print(f"Usuario {usuario.nombre} eliminado por {self.nombre}")

    def modificar_usuario(self, usuario, nuevo_nombre, nuevo_correo):
        """Simula la modificación de un usuario"""
        usuario.nombre = nuevo_nombre
        usuario.correo = nuevo_correo
        print(f"Usuario actualizado por {self.nombre}: {nuevo_nombre}, {nuevo_correo}")