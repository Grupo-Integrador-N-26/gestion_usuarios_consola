import sqlite3
import os

# Ruta a la base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), '../../data/usuarios.db')

def conectar():
    return sqlite3.connect(DB_PATH)

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        rol_id INTEGER NOT NULL,
        FOREIGN KEY (rol_id) REFERENCES roles(id)
    )
    """)

    # Insertar roles si no existen
    cursor.execute("INSERT OR IGNORE INTO roles (id, nombre) VALUES (1, 'admin')")
    cursor.execute("INSERT OR IGNORE INTO roles (id, nombre) VALUES (2, 'usuario')")

    conn.commit()
    conn.close()
