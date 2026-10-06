# blog/operaciones.py

from blog.validaciones import validar_post

def listar_posts(lista_posts):
    if not lista_posts:
        print("No hay posts disponibles.")
        return
    for i, post in enumerate(lista_posts, 1):
        print(f"\n--- Post {i} ---")
        print(f"Título: {post['titulo']}")
        print(f"Autor: {post['autor']['nombre']}")
        print(f"Estado: {post['estado']}")
        print(f"Tags: {', '.join(post['tags'])}")

def buscar_por_titulo(lista_posts, termino):
    termino = termino.lower()
    encontrados = [p for p in lista_posts if termino in p['titulo'].lower()]
    if not encontrados:
        print(f"No se encontraron posts con el título '{termino}'.")
    else:
        print(f"\n--- Resultados de búsqueda ('{termino}') ---")
        for post in encontrados:
            print(f"- {post['titulo']} (Autor: {post['autor']['nombre']})")

def filtrar_por_tag(lista_posts, tag):
    tag = tag.lower()
    encontrados = [p for p in lista_posts if tag in [t.lower() for t in p['tags']]]
    if not encontrados:
        print(f"No hay posts con el tag '{tag}'.")
    else:
        print(f"\n--- Posts con el tag '{tag}' ---")
        for post in encontrados:
            print(f"- {post['titulo']} [Tags: {', '.join(post['tags'])}]")

def validar_todos_los_posts(lista_posts):
    print("\n--- Validación de Posts ---")
    for i, post in enumerate(lista_posts, 1):
        es_valido, mensaje = validar_post(post)
        estado_texto = "VÁLIDO" if es_valido else f"INVÁLIDO ({mensaje})"
        print(f"Post {i} ('{post.get('titulo', 'Sin título')}'): {estado_texto}")
