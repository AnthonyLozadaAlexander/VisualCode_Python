print("Ordenamiento de numeros")
print("-----------------------")

NumArray = [] #Array vacio
CantidadNum = int(input("Ingrese la cantidad de numeros que desea ordenar: "))

for i in range (CantidadNum - 1):
  Numero = int(input(f"Ingrese el numero {i+1}: "))
  NumArray.append(Numero) #? La variable numero se agregara al array
  
for i in range (CantidadNum - 2):
  for j in range (i+1, CantidadNum - 1):
    if NumArray[i] > NumArray[j]:
      
      aux = NumArray[i] #Metodo para intercambiar los valores usando un variable auxiliar.
      NumArray[i] = NumArray[j]
      NumArray[j] = aux
      
           
print(f"El ordenamiento de los numeros es: {NumArray}")