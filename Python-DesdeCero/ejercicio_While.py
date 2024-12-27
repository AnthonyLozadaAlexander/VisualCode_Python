print("Bucle While")
print("------------")
PI = 3.1416

radio = int(input("Ingresar el radio: "))
while (radio < 1):
  
  print("-------------------------------------")
  print("El radio debe ingresar un valor >= 1")
  radio = int(input("Ingrese un radio: "))

area = PI * radio ** 2
print(f"El area usando el radio del circulo es: {area}")
