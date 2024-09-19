'''
cual es el tercer angulo de un triangulo
'''

def calcular_tercer_angulo(angulo1, angulo2):
    # Validar que los ángulos sean enteros positivos
    if angulo1 <= 0 or angulo2 <= 0:
        return "Los ángulos deben ser enteros positivos."

    # Calcular el tercer ángulo
    tercer_angulo = 180 - (angulo1 + angulo2)

    # Validar que el tercer ángulo sea positivo
    if tercer_angulo <= 0:
        return "La suma de los dos ángulos debe ser menor que 180 grados."

    return tercer_angulo


# Ejemplo de uso
angulo1 = int(input("Introduce el primer ángulo (en grados): "))
angulo2 = int(input("Introduce el segundo ángulo (en grados): "))

resultado = calcular_tercer_angulo(angulo1, angulo2)
print(f"El tercer ángulo es: {resultado} grados")