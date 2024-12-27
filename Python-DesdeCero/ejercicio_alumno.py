print("Ejercicio Alumno")
print("---------------------------------------------")

alumno = str(input("Escriba su nombre: "))


calificacion1 = int(input("Ingrese su primera calificacion: "))
calificacion2 = int(input("Ingrese su segunda calificacion: "))
calificacion3 = int(input("Ingrese su tercera calificacion: "))

Promedio = (calificacion1 + calificacion2 + calificacion3 / 3)

while (calificacion1 <= 0 or calificacion1 > 10 or
       calificacion2 <= 0 or calificacion2 > 10 or
       calificacion3 <= 0 or calificacion3 > 10):
  
  print("Las calificaciones deben estar entre 0 y 10")
  
  calificacion1 = int(input("Ingrese su primera calificacion: "))
  calificacion2 = int(input("Ingrese su segunda calificacion: "))
  calificacion3 = int(input("Ingrese su tercera calificacion: "))

print("")  
print("Calificaciones Registradas correctamente")
print("-----------------------------------------")

if Promedio >= 3.5:
  print(f" Felicidades {alumno}, Aprobaste el curso")
  
else:
  
  print(f"{alumno}, Reprobaste el curso")
  
  
print("---------------------------------------------")
