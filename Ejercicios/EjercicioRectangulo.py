def areaRectangulo(base, altura):
  return base * altura

base = 0.0
altura = 0.0

while base <= 0 or altura <= 0:
  
  print("Ingrese la base del rectangulo")
  base = float(input("-> "))
  print("Ingrese la altura del rectangulo")
  altura = float(input("-> "))

  if base <= 0 or altura <= 0:
    print("\nError: Ingrese Valores Mayores a 0\n")
    continue
  
  else:
    print("\nEl area del rectangulo es: ", areaRectangulo(base, altura), "\n")
    break
    

