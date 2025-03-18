matriz = [[0 for _ in range(3)] for _ in range(3)]

# Ingresar los valores de la matriz
for i in range(3): #? Se Ingresa primero a la fila
  for j in range(3): #? Se recorren las columnas
    
    valor = int(input(f"Ingrese el valor de la posicion [{i+1},{j+1}]: "))
    matriz[i][j] = valor

# Mostrar los valores de la matriz    
print("\nLos valores de la matriz son: \n")
for i in range(3):
  for j in range(3):
    print(matriz[i][j], end=" ")
    
  print()
  
# Sumar los valores de la diagonal principal
suma = 0
print("\nLa Diagonal Principal es: \n")
for i in range(3):
  for j in range(3):
    if(i == j):
      suma = suma + matriz[i][j]
      print(matriz[i][j])
      
print("---------------------------------------------------------")
print(f"La suma de la diagonal principal de la matriz es: {suma}")
  

  
  
  
  
