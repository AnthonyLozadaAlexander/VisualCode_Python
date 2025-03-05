#Declara dos variables booleanas y utiliza todos los operadores lógicos para evaluar varias combinaciones, mostrando los resultados por consola.

On = True
Off = False

print(f"On = {On}")
print(f"Off = {Off}\n")

print("----------------------------------------------------")
print("Operadores Logicos\n")
print(f"Operador and: On and Off = {On and Off}")
print(f"Operador or: On or Off = {On or Off}")
print(f"Operador Not: not On = {not On}")
print(f"Operador Not: not Off = {not Off}")
print(f"Operador Not: not On and Off = {not On and Off}") #? False
print(f"Operador Not: not On or Off = {not On or Off}") #? True
print(f"Operador Not: not On and not Off = {not On and not Off}") #? False
print(f"Operador Not: not On or not Off = {not On or not Off}") #? False
print(f"Operador Igual: On == Off = {On == Off}") #? False
print(f"Operador Igual: On == On = {On == On}") #? True
print(f"Operador Igual: Off == Off ={Off == Off}") #? True
print(f"Operador Diferente: On != Off = {On != Off}") #? True
print(f"Operador Diferente: On != On = {On != On}") #? False
print(f"Operador Diferente: Off != Off = {Off != Off}") #? False
print(f"Operador Diferente: not On != Off = {not On != Off}") #? True
print(f"Operador Diferente: not On != On = {not On != On}\n") #? False
print("----------------------------------------------------")