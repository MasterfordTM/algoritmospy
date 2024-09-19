'''
cuanto cuesta un mango
'''

def calcular_costo_total(cantidad, precio_por_mango):
    # Validar entradas
    if cantidad < 0 or precio_por_mango < 0:
        return "La cantidad y el precio deben ser no negativos."

    # Calcular número de conjuntos completos y mangos sobrantes
    conjuntos_completos = cantidad // 3
    mangos_sobrantes = cantidad % 3

    # Calcular costo total
    costo_total = (conjuntos_completos * 2 * precio_por_mango) + (mangos_sobrantes * precio_por_mango)

    return costo_total


# Ejemplo de uso
cantidad = int(input("Introduce la cantidad de mangos: "))
precio_por_mango = float(input("Introduce el precio por mango: "))

costo_total = calcular_costo_total(cantidad, precio_por_mango)
print(f"El costo total por {cantidad} mangos es: ${costo_total:.2f}")