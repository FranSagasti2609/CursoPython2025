#Defino variable inicial y final
numInicial = int(input("Ingresa el numero inicial de la suma: "))
numFinal = int(input("Ingresa el numero final de la suma: "))

#Defino variables para el programa y conteo de numeros
suma = 0
cant_numeros = 0

print(f"Valor inicial: {numInicial} // Valor final: {numFinal}")

#Comienzo a sumar
while numInicial <= numFinal:
    suma = suma + numInicial
    numInicial = numInicial + 1 #incremento en uno el numero
    print(f"Numero actual de conteo: {numInicial-1}")
    cant_numeros = cant_numeros + 1 #aumento el conteo de numeros

#Muestro la suma al finalizar
print(f"El resultado de la suma es: {suma}")