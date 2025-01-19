""" 
array = {1, 2, 3, 4, 5}
print(array, "\n")

print("Agrego 6 y 7 al array\n")
array.update([6, 7])  # Agrega elementos al conjunto array

print(array)

print("--------------------")

for i in array:
    print(i)

"""
print("Ejercicio 4: Suma de elementos de una lista \n")

lista = [1, 2, 3, 5]
suma = sum(lista)
print(f"La suma de los elementos de la lista es: {suma}\n")

print("---------------------------------------------------")

print("Ejercicio 5: Multiplicación de elementos de una lista \n")

lista1 = [1, 2, 3, 5]
mult = 1  # Inicializar mult a 1

for num in lista1:
    mult = mult * num

print(f"La multiplicación de los elementos es: {mult}\n")

print("---------------------------------------------------")
