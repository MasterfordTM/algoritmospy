from PIL import Imagen


def transformar_a_4_3(imagen_path):
    # Cargar la imagen
    imagen = Image.open(imagen_path)

    # Obtener dimensiones originales
    ancho_original, alto_original = imagen.size

    # Calcular nueva anchura (X) para mantener la relación de aspecto 4:3
    nueva_x = round((alto_original * 4) / 3)

    # Redimensionar la imagen a la nueva resolución
    imagen_redimensionada = imagen.resize((nueva_x, alto_original), Image.ANTIALIAS)

    # Guardar la nueva imagen
    nueva_imagen_path = "imagen_transformada_4_3.jpg"
    imagen_redimensionada.save(nueva_imagen_path)

    print(f"La imagen ha sido transformada a 4:3 y guardada como {nueva_imagen_path}")


# Ejemplo de uso
ruta_imagen = input("Introduce la ruta de la imagen: ")
transformar_a_4_3(ruta_imagen)