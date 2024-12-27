# Escribe un programa que reciba un numero entero y calcule la suma de los primeros numeros natuales.

Natural = int(input("Ingresa un Numero Entero: "))
Suma = 0

for i in range(1, Natural +1):
  Suma = Suma + i
  
print(f"La suma de los primeros {Natural} numeros naturales es: {Suma}")