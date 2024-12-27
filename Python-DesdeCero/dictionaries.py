print("Definir un diccionario con la informacion de una Persona")
print("--------------------------------------------------------")

Nombre = str(input("Ingrese su nombre: "))
Edad = int(input("Ingrese su edad: "))
Ciudad = str(input("Ingrese su ciudad: "))

persona = {
  
  "nombre": Nombre,
  "edad": Edad,
  "ciudad": Ciudad,
  
}

# Acceder a valores del diccionario
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])

# Agregar un nuevo valor al diccionario
persona["profesion"] = "Ingeniero"
print("Diccionario despues de agregar a una clave-valor:", persona)

# Eliminar una clave-valor del diccionario
del persona["ciudad"]
print("Diccionario despues de eliminar una clave-valor:", persona)