#Hallar la potencia de dos numeros con sumas

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

potencia = 1
contador = 1

while (contador <= num2): #? esto se puede entender como Mientras contador <= num2
  suma = 0
  condicion = 1
  while (condicion <= num1):
    suma = suma + potencia
    condicion = condicion + 1 #? esto se puede entender como condicion++
  potencia = suma
  contador = contador + 1
  
print(f"El resultado de: {num1} elevado a la potencia {num2} es: {potencia}")