print("Definir una lista de numeros")
print("----------------------------")

numeros = [1, 2, 3, 4, 5] #? Definir una lista de numeros

print("Primer número: ", numeros[0])
print("Ultimo número: ", numeros[-1])

numeros.append(6) #? .append() agrega un elemento al final de la lista
print("Lista despues de agregar un numero: ", numeros)

#Eliminar el ultimo numero de la lista
numeros.pop() #? .pop() elimina el ultimo elemento de la lista
print("Lista despues de eliminar el ultimo numero: ", numeros)