'''
calcula la presion total
'''

def calcular_presion_total(M1, M2, m1, m2, V, T_C):
    # Convertir temperatura de Celsius a Kelvin
    T = T_C + 273.15

    # Constante de gas
    R = 0.082

    # Calcular la presión total usando la fórmula
    P_total = (m1 / M1 + m2 / M2) * R * T / V

    return P_total


# Ejemplo de uso
M1 = float(input("Introduce la masa molar del primer gas (g/mol): "))
M2 = float(input("Introduce la masa molar del segundo gas (g/mol): "))
m1 = float(input("Introduce la masa del primer gas (g): "))
m2 = float(input("Introduce la masa del segundo gas (g): "))
V = float(input("Introduce el volumen del recipiente (dm³): "))
T_C = float(input("Introduce la temperatura (°C): "))

presion_total = calcular_presion_total(M1, M2, m1, m2, V, T_C)
print(f"La presión total es: {presion_total:.2f} atm")