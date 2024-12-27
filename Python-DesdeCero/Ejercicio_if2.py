# Verifica 
#? si el usuario tiene menos de 5 años y si es asi, se imprimira que el boleto sera gratuito,tambien revisa si la edad es entre 5 y 17 años, lo que aplica una tarifa de $50, tambien revisa si la edad es mayor o igual a 60, donde el tambien tambien sera gratuita, si ninguna de las condiciones se cumple, la tarifa estandar sera de $100.

Edad = int(input("Ingrese Su Edad:"))

if Edad < 5:
  print("El Boleto es gratuito para menores de 5 años")
elif Edad <= 17:
  print("El Boleto tiene un precio de $50 Pesos")
elif Edad >= 60:
  print("El Boleto es Gratuito para mayores de 60 años")
else:
  print("El Precio del Boleto es de $100 Pesos para Adultos")
  