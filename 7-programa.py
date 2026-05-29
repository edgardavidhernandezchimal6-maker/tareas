import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Resta Decimal")
ventana.geometry("400x250")

# Etiquetas y entradas
label1 = tk.Label(ventana, text="Introduzca el minuendo:")
label1.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana, text="Introduzca el sustraendo:")
label2.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack()

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=20)

# Función original
def restar():
    minuendo = float(entrada1.get())
    sustraendo = float(entrada2.get())
    resultado.config(text="Resultado de la resta: " + str(minuendo - sustraendo))

# Ejecutar al presionar Enter
ventana.bind(
    "<Return>",
    lambda event: restar()
)

# Iniciar ventana
ventana.mainloop()
