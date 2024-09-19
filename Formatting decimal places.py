def redondear_a_dos_decimales(numero):
    # Redondear el número a dos decimales
    return f"{round(numero, 2):.2f}"

# Ejemplo de uso
numero = float(input("Introduce un número: "))
resultado = redondear_a_dos_decimales(numero)
print(f"El número redondeado a dos decimales es: {resultado}")