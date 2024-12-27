print("Algoritmo para calcular el residuo de una division")
print("--------------------------------------------------")

print("Recordar que no se puede dividir por 0")
print("")

num = int(input("Ingrese el primer numero: "))
divisor = int(input("Ingrese el divisor: "))

residuo = num % divisor

print("")

print(f"El residuo de la division entre {num} y {divisor} es: {residuo}")