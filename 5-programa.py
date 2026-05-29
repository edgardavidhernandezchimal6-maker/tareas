import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Suma Decimal")
ventana.geometry("400x250")

# Etiquetas y entradas
label1 = tk.Label(ventana, text="Introduzca el primer sumando (Decimal):")
label1.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana, text="Introduzca el segundo sumando (Decimal):")
label2.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack()

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=20)

# Función original
def sumar():
    sumando1 = float(entrada1.get())
    sumando2 = float(entrada2.get())
    resultado.config(text="Resultado de la suma: " + str(sumando1 + sumando2))

# Ejecutar al presionar Enter
ventana.bind(
    "<Return>",
    lambda event: sumar()
)

# Iniciar ventana
ventana.mainloop()
