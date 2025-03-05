import os

On = True

name = str(input("Ingrese su nombre: "))
pago = float(input("Ingrese el monto a pagar: "))

while On:
  os.system('cls')
  print("Con que tarjeta desea pagar?")
  print("Digite 1 para Sams CLASICA")
  print("Digite 2 para Sams GOLDEN\n")
  Tarjeta = int(input("Digite el numero de la tarjeta: "))
  
  if Tarjeta == 1:
    Descuento = pago * 0.20
    print("")
    print(f"Estimad@ {name}")
    print(f"Su pago se ha realizado con Exito")
    print(f"Su descuento usando Sams CLASICA es de: {Descuento}")
    On = False
    
  elif Tarjeta == 2:
    Descuento = pago * 0.30
    print("")
    print(f"Estimad@ {name}")
    print(f"Su pago se ha realizado con Exito")
    print(f"Su descuento usando Sams GOLDEN es de: {Descuento}")
    On = False
    
  else:
    print("")
    print("Vuelva a intentarlo")
    print("Digite una opcion valida\n")
    On = True



