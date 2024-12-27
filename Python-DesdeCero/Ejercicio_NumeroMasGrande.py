# Determinar 
#? Cual numero es el mas grande de los 3 ingresados por teclado.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num1 >= num2 and num1 >= num3:
  print(f"el numero {num1} es el numero mas grande")

elif num2 >= num1 and num2 >= num3:
  print(f"el numero {num2} es el numero mas grande")
  
else:
  print(f"el numero {num3} es el numero grande")