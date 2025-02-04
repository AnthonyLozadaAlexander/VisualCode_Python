print("Programa para hacer operaciones aritmeticas basicas")
print("---------------------------------------------------\n")

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

On = 1

while On == 1:
  
  print("SELECCCIONE UNA OPCION PARA VER TEXTO, TIENE QUE SER UN NUMERO DEL 1 AL 3")
  print("1.- Suma")
  print("2.- Resta")
  print("3.- Multiplicacion")

  op = int(input("Opcion: "))

  def case_1():
    return a + b

  def case_2():
    return a - b

  def case_3():
    return a * b

  switch = {
    1: case_1(),
    2: case_2(),
    3: case_3()
  }

  result = switch.get(op, lambda:"Opcion Invalida")
  print(f"Resultado: {result}\n")
  
  On = int(input("Desea hacer otra operacion? 1 = Si, 0 = No: "))
  
  if On == 0:
    
    On = 0
    print("Gracias por usar el programa")
    
  elif On == 1:
    
    On = 1
    print("")
    
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    
  else:
    print("Error404")
    Onn = 0;