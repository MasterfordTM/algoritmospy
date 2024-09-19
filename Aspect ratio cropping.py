'''
Recorte de relación de aspecto
'''


def convertir_a_16_9(resolucion_x, resolucion_y):
    # Verificar que la altura (Y) sea válida
    if resolucion_y <= 0:
        raise ValueError("La altura debe ser un número entero positivo.")

    # Calcular la nueva anchura (X) para mantener la relación de aspecto 16:9
    nueva_x = round((resolucion_y * 16) / 9)

    # Devolver la nueva resolución en formato [X, Y]
    return [nueva_x, resolucion_y]


# Ejemplo de uso
resolucion_x = int(input("Introduce la resolución X: "))
resolucion_y = int(input("Introduce la resolución Y: "))

resultado = convertir_a_16_9(resolucion_x, resolucion_y)
print(f"La nueva resolución con relación de aspecto 16:9 es: {resultado}")