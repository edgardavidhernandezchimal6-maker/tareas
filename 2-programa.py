import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Programa")
ventana.geometry("400x150")

# Resultados originales
resultado1 = "1 2 3 4 5"
resultado2 = "1,2,3,4,5"

# Mostrar resultados en la ventana
mensaje1 = tk.Label(ventana, text=resultado1)
mensaje1.pack(pady=10)

mensaje2 = tk.Label(ventana, text=resultado2)
mensaje2.pack()

# Iniciar ventana
ventana.mainloop()
