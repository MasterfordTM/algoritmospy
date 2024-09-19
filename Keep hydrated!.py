import math


def calcular_litros_bebidos(horas):
    # Validar que las horas sean un número positivo
    if horas < 0:
        return "El tiempo debe ser un número positivo."

    # Calcular la cantidad de litros
    litros = horas * 0.5

    # Redondear hacia abajo al valor más pequeño
    litros_redondeados = math.floor(litros)

    return litros_redondeados


# Ejemplo de uso
horas_ciclismo = float(input("Introduce el tiempo en horas de ciclismo: "))
resultado = calcular_litros_bebidos(horas_ciclismo)
print(f"Nathan beberá {resultado} litros de agua.")