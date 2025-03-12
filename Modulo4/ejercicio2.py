#Funcion para ingresar los 10 numeros
def llenarLista(miLista):
    while(len(miLista)<11):
        numero = int(input("Ingrese un numero para la lista:"))
        miLista.append(numero)

#Funcion estadistica
def analizar(miLista):
    print(f"La lista de numeros que has ingresado, ordenada ascendientemente es: {sorted(miLista)}")
    print(f"La suma de los elementos de la lista es: {sum(miLista)}")
    print(f"La cantidad de elementos de la lista es: {len(miLista)}")
    print(f"El promedio de los elementos de la lista es: {sum(miLista)/len(miLista)}")
    print(f"El valor maximo de la lista es: {max(miLista)}")
    print(f"El valor minimo de la lista es: {min(miLista)}")

#LLamo a las funciones para agregar datos y mostrar informacion

listaNum = [] #defino lista vacia
llenarLista(listaNum)
analizar(listaNum)