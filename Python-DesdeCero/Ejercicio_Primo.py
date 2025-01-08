#Ejercicio_Primo.py

num = int(input("Ingrese un numero: "))

esPrimo = True
if num <= 1:
  esPrimo = False
else:
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      esPrimo = False
      break
    
if esPrimo:
  print(f"El numero {num} es primo")
else:
  print("El numero {num} no es primo")