print("Algoritmo para sumar los elementos de un array\n")
print("Ingrese el tamaño del array: ")

n = int(input()) #Entrad
array = []
suma = 0

for i in range(n):
    print("Ingrese el valor de la posición ", i)
    array.append(int(input())) #append agrega un elemento al final de la lista
    suma = suma + array[i]
    print("")
    
print("El array es: ", array)
print(f"La suma de los elementos del array es: {suma}")


