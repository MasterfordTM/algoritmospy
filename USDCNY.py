def convertir_usd_a_cny(cantidad_usd):
    # Tasa de cambio (puedes actualizar esta tasa según el mercado actual)
    tasa_cambio = 6.45  # Ejemplo: 1 USD = 6.45 CNY (esta tasa puede variar)

    # Validar que la cantidad de USD sea un número entero positivo
    if cantidad_usd < 0:
        return "La cantidad de dólares debe ser un número entero positivo."

    # Calcular la cantidad en yuanes
    cantidad_cny = cantidad_usd * tasa_cambio

    # Formatear el resultado como una cadena
    resultado = f"{cantidad_cny:.2f} Yuan chino"

    return resultado


# Ejemplo de uso
cantidad_dolares = int(input("Introduce la cantidad en dólares estadounidenses (USD): "))
resultado_conversion = convertir_usd_a_cny(cantidad_dolares)
print(resultado_conversion)