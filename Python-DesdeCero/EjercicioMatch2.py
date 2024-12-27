def dia_de_la_semana(dia):
    match dia:
        case 1:
           return "Lunes"
        case 2:
           return "Martes"
        case 3:
           return "Miercoles"
        case 4:
           return "Jueves"
        case 5:
           return "Viernes"
        case 6:
           return "Sabado"
        case 7:
           return "Domingo"
          
for i in range(8):
    print(f"El dia {1} es {dia_de_la_semana(i)}")