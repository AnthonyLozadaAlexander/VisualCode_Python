n = int(input("Ingrese la cantidad de n numeros naturales: "))

while n <= 0:

    print("\nError: El numero debe ser mayor a 0\n")
    n = int(input("Ingrese un numero mayor a 0: "))

suma = 0
for i in range(1, n+1):
    cuadrados = (i**2)
    suma = suma + cuadrados

print(
    f"\nLa suma de los cuadrados de los primeros {n} numeros naturales es: {suma}\n")
