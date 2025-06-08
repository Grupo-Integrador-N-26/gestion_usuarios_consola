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

## Cómo ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Grupo-Integrador-N-26/gestion_usuarios_consola.git

2. ```
    cd gestion_usuarios_consola
  
3. Asegurarce de tener Python instalado:
  ```
  python --verision
```
4. Ejecuta el programa
 ```
  python src/main.py
```

## Contribuciones

¡Las contribuciones son bienvenidas!

1. Haz un fork del repositorio.

2. Crea una nueva rama:
``` bash
    git checkout -b feacture/nueva-funcionalidad
```
3. Realiza tus cambios y haz un commit:
``` bash
    git commit -m "Agrega nueva funcionalidad"
```
4. Sube tus cambios 
```bash 
   git push origin feacture/nueva-funcionalidad
```
5. Abre un Pull Request.


## 👤 Autor
         Mayco David Ardiles

- Organización: **Grupo Integrador Nº 26**         
- Proyecto académico/práctico para el desarrollo de habilidades en programación, diseño de bases de datos y control de versiones.
