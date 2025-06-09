import sqlite3

DB_PATH = "data/usuarios.db"

class Usuario:
    def __init__(self, username, password, rol_id=2):
        self.username = username
        self.password = password
        self.rol_id = rol_id  # 1 = admin, 2 = estándar

    def registrar(self):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (username, password, rol_id) VALUES (?, ?, ?)",
                    (self.username, self.password, self.rol_id)
                )
                conn.commit()
                print(f" Usuario '{self.username}' registrado correctamente.")
        except sqlite3.IntegrityError:
            print(f" El nombre de usuario '{self.username}' ya existe.")
        except Exception as e:
            print(f" Error al registrar usuario: {e}")

    def eliminar(self):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM users WHERE username = ?",
                    (self.username,)
                )
                conn.commit()
                print(f" Usuario '{self.username}' eliminado.")
        except Exception as e:
            print(f" Error al eliminar usuario: {e}")

    def mostrar_info(self):
        print(f" Usuario: {self.username}, Rol ID: {self.rol_id}")
