class Usuario:
    def __init__(self, nombre_usuario, contraseña, perfil):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.perfil = perfil  # instancias de Rol

    def es_contraseña_valida(self):
        tiene_longitud = len(self.contraseña) >= 6
        tiene_letra = any(c.isalpha() for c in self.contraseña)
        tiene_numero = any(c.isdigit() for c in self.contraseña)
        return tiene_longitud and tiene_letra and tiene_numero