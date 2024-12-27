print("Ejercicio IMC")
print("--------------")

print("Ingrese su peso en kilogramos: ")
Peso = float(input())

print("")

print("Ingrese su altura en metros: ")
Altura = float(input())

imc = (Peso / (Altura ** 2))

print("")

print(f"Su indice de masa coporal es: {imc}")