matriz = [[0 for _ in range(3)] for _ in range(3)]

# Ingresar los valores de la matriz
for i in range(3):
  for j in range(3):
    valor = int(input(f"Ingrese el valor de la posicion [{i+1},{j+1}]: "))
    matriz[i][j] = valor

# Mostrar los valores de la matriz    
print("Los valores de la matriz son: ")
for fila in matriz:
  for valor in fila:
    print(valor, end=" ")
  print()
  

  
  
  
  
