print("Tabla de multiplicar del numero ingresado del 1 hasta al 10")
print("-----------------------------------------------------------")

num = int(input("Ingrese un numero: "))

for i in range (1, 10):
  Calculo = num * i
  print(f"La tabla del {num} es: {Calculo}")