import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Cadenas")
ventana.geometry("400x150")

# Variable original
cadenaejemplo = "Hola Time of Software"

# Mostrar texto en la ventana
mensaje = tk.Label(ventana, text=cadenaejemplo)
mensaje.pack(pady=40)

# Iniciar ventana
ventana.mainloop()
