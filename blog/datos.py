# blog/datos.py

perfil_autor = {
    "nombre": "Maia",
    "email": "maia@example.com"
}

estados_post = ["borrador", "publicado", "archivado"]

etiquetas_blog = ["python", "programacion", "modular", "git"]

posts = [
    {
        "titulo": "Introduccion a Python",
        "contenido": "Python es un lenguaje de programación versátil y potente.",
        "autor": perfil_autor,
        "tags": ["python", "programacion"],
        "estado": "publicado"
    },
    {
        "titulo": "Organizacion Modular",
        "contenido": "Separar el código en módulos facilita el mantenimiento.",
        "autor": perfil_autor,
        "tags": ["modular", "programacion"],
        "estado": "publicado"
    }
]
