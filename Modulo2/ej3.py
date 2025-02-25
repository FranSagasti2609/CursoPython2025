#Defino funcion para comparar dos numeros
def compararNum(a,b):
 if(a>b):
  return a
 else: 
  if(a<b):
   return b
  else:
   if(a==b):#caso que sean iguales se retorna cualquiera
    return a
   
#Solicitamos numeros
num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))

print(f"El numero mas alto es: {compararNum(num1,num2)}")