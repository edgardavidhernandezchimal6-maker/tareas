import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Cadena Multilínea")
ventana.geometry("400x200")

# Variable original
cadenaejemplo = "Hola Time of Software\nEsto es una cadena\nmultilinea"

# Mostrar texto en la ventana
mensaje = tk.Label(ventana, text=cadenaejemplo)
mensaje.pack(pady=30)

# Iniciar ventana
ventana.mainloop()
