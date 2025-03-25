def solicitarNumero():
    numero = int(input("Ingrese un numero: "))
    return numero

def solicitarOperacion():
    operacion = input("Ingrese una operacion: +, -, *, /: ")
    return operacion

def operar(num1, num2, cuenta):
    if(cuenta=="+"):
        return num1 + num2
    elif(cuenta=="-"):
        return num1 - num2
    elif(cuenta=="*"):
        return num1*num2
    else:
        if(num2!=0):
            return num1/num2
        else:
            print("El segundo numero debe ser diferente de cero si deseas dividir.")
 
#Main
num1 = solicitarNumero()
num2 = solicitarNumero()
operador = solicitarOperacion()

resultado = operar(num1,num2, operador)

print(f"El resultado de su operacion es: {resultado}")
