from permiso import Permiso

class Rol:
    def __init__(self, nombre):
        self.nombre = nombre
        self.permisos = []

    def agregar_permiso(self, permiso):
        self.permisos.append(permiso)

    def tiene_permiso(self, nombre_permiso):
        return any(p.nombre == nombre_permiso for p in self.permisos)