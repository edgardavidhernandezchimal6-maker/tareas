import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Programa")
ventana.geometry("400x150")

# Resultado original
resultado = "1,2,3,4,5."

# Mostrar resultado en la ventana
mensaje = tk.Label(ventana, text=resultado)
mensaje.pack(pady=40)

# Iniciar ventana
ventana.mainloop()
