x = 3
y = 5

print(x == y) #? sirve para comparar si son "iguales" y decirme si es true or false

print()

print(x != y) #? sirve para comparar si son "diferentes" y decirme si es true or false

print()

print("Calculo Factorial De Un Numero")
print()

n = int(input("Ingrese un numero: "))
factorial = 1

for i in range (1, n+1):
  factorial = factorial * 1
  
print(f"El factorial de {n} es {factorial}")

print()
print("Verificar si un numero es primo")

n1 = int(input("Ingrese un numero: "))
esPrimo = True #? el valor por defecto es true

if n1 <= 1: #? si el numero ingresado es menor o igual a 1, entonces no puede ser primo
  esPrimo = False #? si no es primo, sera false
else:
  for i in range(2, n):
    if n1 % 1 == 0:
     esPrimo = False
     
if esPrimo == True:
  print(f"{n1} es un numero primo")
else:
  print(f"{n1} no es numero primo")
  
  