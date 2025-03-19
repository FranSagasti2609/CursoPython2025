# Función para solicitar una tupla de números enteros, similar al visto en el ej2
def ingresar_tupla():
    return tuple(map(int, input("Ingrese los números de la tupla separados por espacio: ").split()))

# Solicitamos las tuplas al usuarip
tupla1 = ingresar_tupla()
tupla2 = ingresar_tupla()

# Verificar que ambas tuplas tengan la misma longitud
if len(tupla1) != len(tupla2):
    print("Error: Las tuplas deben tener la misma longitud.")
else:
    # Multiplicar elemento por elemento usando comprensión de tuplas
    tupla_resultante = tuple(a * b for a, b in zip(tupla1, tupla2))

    # Mostrar la tupla resultante
    print("Tupla resultante:", tupla_resultante)
