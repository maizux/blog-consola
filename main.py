# main.py

from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag, validar_todos_los_posts

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            listar_posts(posts)
        elif opcion == "2":
            termino = input("Ingresa el término a buscar en el título: ")
            buscar_por_titulo(posts, termino)
        elif opcion == "3":
            tag = input("Ingresa el tag a filtrar: ")
            filtrar_por_tag(posts, tag)
        elif opcion == "4":
            validar_todos_los_posts(posts)
        elif opcion == "5":
            print("¡Gracias por usar el sistema del blog! Hasta luego.")
            break
        else:
            print("Opción inválida. Por favor, elige un número entre 1 y 5.")

if __name__ == "__main__":
    main()
