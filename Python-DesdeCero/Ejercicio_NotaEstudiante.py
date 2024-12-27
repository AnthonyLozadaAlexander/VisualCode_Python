print("Calcular La Nota Del Estudiante")

print("");

Nombre = str(input("Ingrese su Nombre:"))
Calificacion = float(input("Ingrese su calificacion:"))

if Calificacion >= 90:
  print(f"Felicidades!{Nombre} Has Aprobado Con Una Nota Sobresaliente")
elif Calificacion >= 70 and Calificacion < 90:
  print("Has Aprobado Satisfactoriamente")
elif Calificacion >= 60 and Calificacion < 70:
  print("Has Aprobado Pero Necesitas Mejorar")
  
else:
  print(f"Losiento {Nombre}, Has Suspendido. Debes Esforzarte Mas En La Proxima")
