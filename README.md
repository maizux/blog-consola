# Blog de Consola - Modularizado (Preentrega 5)

## Qué hace el programa
Es un sistema por consola modularizado en Python que permite gestionar, listar, buscar por título, filtrar por etiquetas (tags) y validar la estructura de los posts de un blog.

## Cómo está organizada la carpeta
```text
blog_consola/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada módulo
- **`main.py`**: Archivo principal de ejecución. Orquesta el flujo del menú y coordina las llamadas a las funciones de los distintos módulos usando bloques protegidos con `if __name__ == "__main__":`.
- **`blog/datos.py`**: Contiene las estructuras de base de datos del sistema (`posts`, `perfil_autor`, `etiquetas_blog`, etc.).
- **`blog/menu.py`**: Maneja la interacción con el usuario mostrando las opciones disponibles y capturando el `input()`.
- **`blog/operaciones.py`**: Agrupa la lógica principal de negocio (listar, buscar por título, filtrar por tag).
- **`blog/validaciones.py`**: Contiene las reglas lógicas para validar que la estructura y los tipos de datos de los posts sean correctos.

## Cómo ejecutar el sistema
Desde la carpeta raíz del proyecto (`blog_consola/`), ejecuta el siguiente comando en la terminal:
```bash
python main.py
```
