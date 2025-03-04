#Defino variable para guardar la cantidad de "a"
cant_letra = 0

cadena = "programacion"

for letra in cadena:
    if letra == "a":
        cant_letra=cant_letra+1

print(f"La palabra {cadena} tiene {cant_letra} veces la letra A.")