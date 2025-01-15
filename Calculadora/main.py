from tkinter import*

raiz = Tk()
raiz.geometry("700x700") #? ventana de 700x700
raiz.title("Calculadora Anthony") #* Titulo de la ventana
raiz.config(bg = "white") #? Background, color de fondo

#? Variable r
r = DoubleVar()

pantalla = Entry(bg = "green", foreground = "black", font = "Miracode 14 bold", textvariable = r) #* Entry es para que se pueda escribir en la pantalla
pantalla.grid(row = 2, column = 2)

#? Variables
num1 = DoubleVar()
num2 = DoubleVar()


#* Entrada 1
texto1 = Label(font = "Miracode 14", text = "Primer Valor")
texto1.grid(row = 3, column = 1)
campo1 = Entry(font = "Miracode 14", textvariable = num1)
campo1.grid(row = 3, column = 2, padx = 5)

#* Entrada 2
texto2 = Label(font = "Miracode 14", text = "Segundo Valor")
texto2.grid(row = 4, column = 1)
campo2 = Entry(font = "Miracode 14", textvariable = num2)
campo2.grid(row = 4, column = 2, padx = 5)

raiz.mainloop()