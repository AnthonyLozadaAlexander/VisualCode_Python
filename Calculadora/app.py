from tkinter import *
import ast

Window = Tk() #?Instancia para crear la ventana
Window.title("Calculator") #?Asignarle titulo a la ventana
#Window.geometry("125x125")
Window.eval('tk::PlaceWindow . center')

display = Entry(Window) #?Crear un espacio de texto
display.grid(row=1, columnspan=6, sticky=W+E) #*Creacion de la grid del espacio de la ventana

i = 0 #?Variable para el indice de la lista de numeros

#Funcion para obtener los numeros que se presionan en la calculadora
def get_numbers(n):
  global i
  display.insert(i, n)
  i = i + 1
  
#Funcion para obtener las operaciones que se presionan en la calculadora
def get_operation(operator):
  global i
  operator_length = len(operator)
  display.insert(i, operator)
  i = i + operator_length

#Funcion para limpiar el display
def clear_display():
  display.delete(0, END)
  
#Funcion para borrar el ultimo caracter
def undo():
  display_state = display.get()
  if len(display_state):
    display_new_state = display_state[:-1]
    clear_display()
    display.insert(0, display_new_state)
  # Eliminado el mensaje de error cuando el display está vacío
    
def calculate():
    display_state = display.get()
    try:
        # Correctly chain replace calls to handle all replacements
        math_expr = (
            display_state
            .replace("x", "*")
            .replace("^", "**")
            .replace("exp", "**")
        )
        # Usar eval en lugar de ast.literal_eval para admitir más operaciones matemáticas
        result = eval(math_expr)
        clear_display()
        display.insert(0, result)
    except SyntaxError:
        clear_display()
        display.insert(0, "Syntax Error")
    except ZeroDivisionError:
        clear_display()
        display.insert(0, "Division by Zero")
    except Exception as e:
        clear_display()
        display.insert(0, "Error")

#Row = fila, Column = columna
#sticky = W+E -> Que se expanda de izquierda a derecha
#command = lambda:get_numbers() -> funcion que nos permite obtener los numeros que se presionan en la calculadora

#Numeric Buttons
Button(Window, text="1", command = lambda:get_numbers(1)).grid(row=2, column=0, sticky=W+E)
Button(Window, text="2", command = lambda:get_numbers(2)).grid(row=2, column=1, sticky=W+E)
Button(Window, text="3", command = lambda:get_numbers(3)).grid(row=2, column=2, sticky=W+E)

Button(Window, text="4", command = lambda:get_numbers(4)).grid(row=3, column=0, sticky=W+E)
Button(Window, text="5", command = lambda:get_numbers(5)).grid(row=3, column=1, sticky=W+E)
Button(Window, text="6", command = lambda:get_numbers(6)).grid(row=3, column=2, sticky=W+E)

Button(Window, text="7", command = lambda:get_numbers(7)).grid(row=4, column=0, sticky=W+E)
Button(Window, text="8", command = lambda:get_numbers(8)).grid(row=4, column=1, sticky=W+E)
Button(Window, text="9", command = lambda:get_numbers(9)).grid(row=4, column=2, sticky=W+E)

#Buttons Operations
Button(Window, text="AC", command=lambda: clear_display()).grid(row=5, column=0, sticky=W+E)
Button(Window, text="0", command = lambda:get_numbers(0)).grid(row=5, column=1, sticky=W+E)
Button(Window, text=".", command=lambda: get_numbers(".")).grid(row=5, column=1, sticky=W+E)
Button(Window, text="%", command = lambda:get_operation("%")).grid(row=5, column=2, sticky=W+E)

Button(Window, text="+", command=lambda:get_operation("+")).grid(row=2, column=3, sticky=W+E, columnspan=2)
Button(Window, text="-", command = lambda:get_operation("-")).grid(row=3, column=3, sticky=W+E)
Button(Window, text="x", command = lambda:get_operation("x")).grid(row=4, column=3, sticky=W+E)
Button(Window, text="/", command = lambda:get_operation("/")).grid(row=5, column=3, sticky=W+E)

Button(Window, text="exp", command=lambda: get_operation("exp")).grid(row=3, column=4, sticky=W+E)
Button(Window, text="^2", command=lambda: get_operation("^2")).grid(row=3, column=5, sticky=W+E)
Button(Window, text="(", command=lambda: get_operation("(")).grid(row=4, column=4, sticky=W+E)
Button(Window, text=")", command=lambda: get_operation(")")).grid(row=4, column=5, sticky=W+E)
Button(Window, text="🠈", command=lambda: undo()).grid(row=2, column=4, sticky=W+E, columnspan = 2)
Button(Window, text="=", command=lambda: calculate()).grid(row=5, column=4, sticky=W+E, columnspan = 2)


Window.mainloop() #?Mantener la ventana abierta