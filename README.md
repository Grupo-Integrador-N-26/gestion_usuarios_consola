# Gestión de Usuarios en Consola

Este proyecto es una aplicación de consola escrita en Python que permite la administración de usuarios con control de acceso por roles (Administrador y Usuario Estándar), utilizando una base de datos SQLite para almacenar y gestionar la información.

## Objetivo

Desarrollar un programa de consola interactivo que permita:

- Registrar usuarios con validaciones.
- Iniciar sesión con credenciales.
- Controlar el acceso según el rol del usuario.
- Gestionar usuarios (crear, eliminar, visualizar).
- Brindar una experiencia intuitiva desde la terminal.

## Funcionalidades principales

- Autenticación de usuarios con contraseña segura.
- Diferenciación de roles y permisos.
- Gestión CRUD de usuarios (según permisos).
- Menú interactivo en consola.
- Persistencia de datos con SQLite.

## Tecnologías usadas

- Python 3.x
- SQLite
- Programación Orientada a Objetos
- Git

## Estructura del proyecto

```
gestion_usuarios_consola/
├── src/ # Código fuente principal
│ ├── database/ # Módulo para conexión y operaciones con SQLite
│ ├── models/ # Clases como Usuario, Administrador
│ ├── utils/ # Funciones auxiliares, validaciones, etc.
│ └── main.py # Punto de entrada del programa
├── data/ # Base de datos SQLite
├── README.md
```
