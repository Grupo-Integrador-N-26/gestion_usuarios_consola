# Gestión de Usuarios en Consola

Este proyecto es una aplicación de consola desarrollada en Python que permite la administración de usuarios con roles diferenciados (Administrador y Usuario Estándar). Utiliza SQLite como sistema de gestión de base de datos para almacenar los datos de forma persistente.

## Objetivo

Desarrollar un sistema de gestión de usuarios que permita:

- Registrar usuarios con validaciones.
- Iniciar sesión mediante credenciales almacenadas.
- Diferenciar el acceso según el rol del usuario.
- Gestionar usuarios desde una interfaz de consola intuitiva. 

## Funcionalidades principales

- Registro de usuarios con validación de contraseña.
- Permisos diferenciados según rol:

          -Administrador: acceso total (crear, ver, eliminar usuarios, etc.).

        -Usuario estándar: acceso restringido (solo ver su información).

- Control de acceso mediante menú interactivo.
- Manejo de errores y mensajes informativos.
- 

## Tecnologías usadas

- Python 3.x
- SQLite
- Entorno de desarrollo: Visual Studio Code
- Git

## Estructura del proyecto

```
gestion_usuarios_consola/
├── src/ # Código fuente
│ ├── database/ # Conexión y operaciones con SQLite
│ ├── models/ # Clases: Usuario, Admin, etc.
│ ├── utils/ # Funciones auxiliares, validaciones, etc.
│ └── main.py # Archivo principal
├── data/ # Archivo de base de datos SQLite
├── README.md # Documentación del proyecto
```
