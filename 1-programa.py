import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Programa Hola")
ventana.geometry("400x150")

# Mensajes en la ventana
mensaje1 = tk.Label(ventana, text="¡Hola Time of Software!")
mensaje1.pack(pady=10)

mensaje2 = tk.Label(ventana, text="Este es mi primer programa con Python")
mensaje2.pack()

# Iniciar ventana
ventana.mainloop()
