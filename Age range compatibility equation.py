'''
calcular rangos de edad
'''

import math


def calcular_rango_edad(age):
    # Validar que la edad esté dentro del rango permitido
    if age < 1 or age > 100:
        return "La edad debe estar entre 1 y 100."

    if age <= 14:
        # Fórmulas para edades menores o iguales a 14
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        # Fórmulas para edades mayores a 14
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor(age * 2 - 7)

    return f"{min_age}-{max_age}"


# Ejemplo de uso
edad = int(input("Introduce tu edad (1-100): "))
rango_edad = calcular_rango_edad(edad)
print(f"El rango de edad recomendado es: {rango_edad}")