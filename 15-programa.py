import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Lista")
ventana.geometry("400x150")

# Variable original
lista = ["ordenador", "teclado", "raton"]

# Mostrar lista en la ventana
mensaje = tk.Label(ventana, text=str(lista))
mensaje.pack(pady=40)

# Iniciar ventana
ventana.mainloop()
