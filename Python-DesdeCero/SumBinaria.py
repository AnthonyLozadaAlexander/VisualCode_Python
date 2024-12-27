print("Algoritmo para una suma binaria")
print("--------------------------------")

# Ingresar los números binarios
Binario1 = input("Ingrese un número binario: ")
Binario2 = input("Ingrese otro número binario: ")

# Validar que las entradas sean binarios válidos
while not (Binario1.isdigit() and Binario2.isdigit() and
           all(c in '01' for c in Binario1) and all(c in '01' for c in Binario2)):
    print("Ambos números deben ser binarios válidos.")
    Binario1 = input("Ingrese un número binario: ")
    Binario2 = input("Ingrese otro número binario: ")

# Alinear las longitudes añadiendo ceros a la izquierda
max_longitud = max(len(Binario1), len(Binario2))
Binario1 = Binario1.zfill(max_longitud)
Binario2 = Binario2.zfill(max_longitud)

# Inicializar variables
acarreo = 0
resultado = ""

# Realizar la suma binaria desde el final hacia el inicio
for i in range(max_longitud - 1, -1, -1):
    bit1 = int(Binario1[i])
    bit2 = int(Binario2[i])
    suma = bit1 + bit2 + acarreo
    
    if suma == 2:
        resultado = "0" + resultado
        acarreo = 1
    elif suma == 3:
        resultado = "1" + resultado
        acarreo = 1
    else:
        resultado = str(suma) + resultado
        acarreo = 0

# Si queda un acarreo, agregarlo al resultado
if acarreo == 1:
    resultado = "1" + resultado

print(f"El resultado de la suma es: {resultado}")
  