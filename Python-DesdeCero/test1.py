import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")

etiqueta = tk.Label(ventana, text= "Hola, Mundo!")
etiqueta.pack()

ventana.mainloop()