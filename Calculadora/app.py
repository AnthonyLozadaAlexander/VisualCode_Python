from tkinter import *

Window = Tk() #?Instancia para crear la ventana
Window.title("Calculator") #?Asignarle titulo a la ventana
#Window.geometry("125x125")
Window.eval('tk::PlaceWindow . center')

display = Entry(Window) #?Crear un espacio de texto
display.grid(row=1, columnspan=6, sticky=W+E) #*Creacion de la grid del espacio de la ventana

i = 0 #?Variable para el indice de la lista de numeros

def get_numbers(n):
  global i
  display.insert(i, n)
  i = i + 1


#Row = fila, Column = columna
#sticky = W+E -> Que se expanda de izquierda a derecha

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
Button(Window, text="AC", command=lambda: display.delete(0, END)).grid(row=5, column=0, sticky=W+E)
Button(Window, text="0", command = lambda:get_numbers(0)).grid(row=5, column=1, sticky=W+E)
Button(Window, text="%").grid(row=5, column=2, sticky=W+E)

Button(Window, text="+").grid(row=2, column=3, sticky=W+E)
Button(Window, text="-").grid(row=3, column=3, sticky=W+E)
Button(Window, text="x").grid(row=4, column=3, sticky=W+E)
Button(Window, text="/").grid(row=5, column=3, sticky=W+E)

Button(Window, text="🠈").grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(Window, text="exp").grid(row=3, column=4, sticky=W+E)
Button(Window, text="^2").grid(row=3, column=5, sticky=W+E)
Button(Window, text="(").grid(row=4, column=4, sticky=W+E)
Button(Window, text=")").grid(row=4, column=5, sticky=W+E)
Button(Window, text="=").grid(row=5, column=4, sticky=W+E, columnspan = 2)


Window.mainloop() #?Mantener la ventana abierta