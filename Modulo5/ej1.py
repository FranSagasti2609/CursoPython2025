texto = input("Ingrese una cadena de texto: ")
vocales = 0 #inicio contador en 0

def contarVocales(textito):
    global vocales
    for letra in textito:
        if letra in "aeiouAEIOU":  # Comprobamos si la letra es una vocal
            vocales += 1 

contarVocales(texto)
print(f"La cantidad de vocales es: {vocales}")