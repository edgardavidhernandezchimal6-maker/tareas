import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("División Redondeada")
ventana.geometry("400x250")

# Etiquetas y entradas
label1 = tk.Label(ventana, text="Introduzca el dividendo:")
label1.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana, text="Introduzca el divisor:")
label2.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack()

# Resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack(pady=20)

# Función original
def dividir():
    dividendo = float(entrada1.get())
    divisor = float(entrada2.get())
    resultado = round(dividendo / divisor, 1)

    resultado_label.config(
        text="Resultado de la division: " + str(resultado)
    )

# Ejecutar al presionar Enter
ventana.bind(
    "<Return>",
    lambda event: dividir()
)

# Iniciar ventana
ventana.mainloop()
