# Determinar si un numero es Par o Impar

Numero = int(input("Introduzca Un Numero Entero: "))

#* != (no es igual) , == (igualdad)
match Numero:
  case 0:
    print("El Numero es un cero")
  case Numero if Numero % 2 == 0:
    print("El numero es Par.")
  case Numero if Numero % 2 != 0:
    print("El numero no es Par.")
  case _:
    print("Numero no reconocido")
    
#* case _: se refiere cualquiera cosa que no este relacionado a los casos
    

