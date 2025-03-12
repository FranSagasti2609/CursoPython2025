#Variable para ingresar cant_Estudiantes deseada
cant_Estudiantes = 0

#Variables para contar cantidad de egresos y no exonerados
egresados = 0
noEgresado = 0

#Funcion para ingresar las notas
def llenarLista(miLista):
    global egresados, noEgresado  # Hacemos que las variables sean globales
    while(len(miLista) < cant_Estudiantes):
        numero = int(input("Ingrese una nota: "))
        miLista.append(numero)
        #Contabilizo si pasa o no
        if(numero<5):
            noEgresado = noEgresado +1
        else:
            egresados = egresados +1

def analizar(miLista):
    print(f"Las notas ingresadas ordenadas ascendientemente es: {sorted(miLista)}")
    print(f"El promedio de notas es: {sum(miLista)/len(miLista)}")
    print(f"La cantidad de egresos es: {egresados}")
    print(f"La cantidad de no egresados es: {noEgresado}")

    
listaNum = [] #defino lista vacia
cant_Estudiantes = int(input("Cantidad de notas a ingresar: "))

llenarLista(listaNum)
analizar(listaNum)