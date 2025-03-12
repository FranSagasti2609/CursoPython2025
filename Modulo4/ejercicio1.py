#Funcion promedio
def promedio(numeros):
    if(len(numeros)!=0):
        return sum(numeros)/len(numeros)
    else:
        print("ERROR //// Ingrese una lista con al menos un elemento. ////")
        return 0

listaNumeros = [1,2,3]

#Llamo a la funcion promedio y paso parametro listaNumeros
print(f"El promedio es {promedio(listaNumeros)}")
