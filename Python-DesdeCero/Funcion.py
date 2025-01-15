def obtener_estado():
    print("Patrones Simples\n")
    on = True

    while on:
        status = int(input("Ingrese el estado (200, 400, 500): "))
        if status == 200:
            result = "Ok"
            print(result)
            on = False

        elif status == 400:
            result = "Not Found"
            print(result)

        elif status == 500:
            result = "Server Error"
            print(result)

        else:
            result = "Unknown Status"
            print(result)
            on = False

# Llamada a la función
obtener_estado()