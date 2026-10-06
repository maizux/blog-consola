# blog/validaciones.py

def validar_post(post):
    if not isinstance(post, dict):
        return False, "El post debe ser un diccionario."
    
    claves_necesarias = ["titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_necesarias:
        if clave not in post:
            return False, f"Falta la clave requerida: {clave}"
            
    if not isinstance(post["titulo"], str) or not post["titulo"].strip():
        return False, "El título no puede estar vacío y debe ser texto."
        
    if not isinstance(post["contenido"], str) or not post["contenido"].strip():
        return False, "El contenido no puede estar vacío y debe ser texto."
        
    if not isinstance(post["autor"], dict) or "nombre" not in post:
        return False, "El autor debe ser un diccionario con al menos la clave 'nombre'."
        
    if not isinstance(post["tags"], list):
        return False, "Los tags deben estar guardados como lista."
        
    if post["estado"] not in ["borrador", "publicado", "archivado"]:
        return False, "El estado del post no es válido."
        
    return True, "Post válido."
