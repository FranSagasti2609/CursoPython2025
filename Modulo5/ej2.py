# Solicitar la primera lista de números enteros
lista1 = list(map(int, input("Ingrese la primera lista de números separados por espacio: ").split()))

# Solicitar la segunda lista de números enteros
lista2 = list(map(int, input("Ingrese la segunda lista de números separados por espacio: ").split()))

listFinal = lista1 + lista2

print(f"La lista combina es: {listFinal}")