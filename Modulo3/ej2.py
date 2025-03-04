#Defino variable para guardar la cantidad de "a" y "e"
cant_A = 0
cant_E = 0

cadena = input("Ingrese la palabra donde quiera contar las A y las E: ")

for letra in cadena:
    if letra == "a":
        cant_A = cant_A + 1
    elif letra == "e":
        cant_E = cant_E + 1

print(f"La palabra {cadena} tiene {cant_A} veces la letra A y {cant_E} la letra E")