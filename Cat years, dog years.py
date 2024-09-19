'''
programa que calcula la edada de un gato y un perro
'''

def calculate_animal_ages(humanYears):
    # Inicializamos las edades en años de gato y perro
    cat_years = 0
    dog_years = 0

    # Calculamos la edad del gato
    if humanYears >= 1:
        cat_years += 15
    if humanYears >= 2:
        cat_years += 9
    if humanYears > 2:
        cat_years += (humanYears - 2) * 4

    # Calculamos la edad del perro
    if humanYears >= 1:
        dog_years += 15
    if humanYears >= 2:
        dog_years += 9
    if humanYears > 2:
        dog_years += (humanYears - 2) * 5

    # Devolvemos las edades en la forma deseada
    return [humanYears, cat_years, dog_years]


# Ejemplo de uso
print(calculate_animal_ages(1))  # Output: [1, 15, 15]
print(calculate_animal_ages(2))  # Output: [2, 24, 24]
print(calculate_animal_ages(3))  # Output: [3, 28, 29]
print(calculate_animal_ages(5))  # Output: [5, 36, 39]
