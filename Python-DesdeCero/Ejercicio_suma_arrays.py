print("Suma de numeros en un array")
print("----------------------------")


NumArray = [0] #Inicializo la variable en 0

CantidadNumeros = int(input("Ingrese la cantidad de numeros que desea sumar: "))
for i in range (CantidadNumeros): #? Recorrera la cantidad de numeros que se ingresen.
 
  Numero = int(input(f"Ingrese el numero {i+1}: "))
  NumArray.append(Numero)
  
#* Calculo de la suma del array.
suma = sum(NumArray)

print(f"La suma de los numeros es: {suma}")