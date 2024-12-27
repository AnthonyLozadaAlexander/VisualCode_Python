print("Ejercicio Fibonacci")
print("-------------------")

a = 0
b = 1
i = 0

n = int(input("Ingrese la cantidad de numeros que desea generar: "))

print("Secuencia de fibonacci: ")

for i in range (0, n):
  print(a, " ")
  c = (a + b)
  a = b
  b = c
  
print("--------------------------------------------------------")
print("Fin del Programa")