# Función para ingresar una lista de palabras
def ingresar_palabras():
    palabras = []
    while True:
        palabra = input("Ingrese una palabra (o presione Enter para terminar): ")
        if palabra == "":  # Si el usuario presiona Enter sin escribir, termina el ingreso
            break
        palabras.append(palabra)
    return palabras

# Solicitar la lista de palabras
lista_palabras = ingresar_palabras()

# Verificar que haya al menos una palabra en la lista
if lista_palabras:
    # Determinar la palabra más larga utilizando la función max() con la clave len
    palabra_mas_larga = max(lista_palabras, key=len)
    print("La palabra más larga es:", palabra_mas_larga)
else:
    print("No se ingresaron palabras.")
