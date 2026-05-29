import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Multiplicación Decimal")
ventana.geometry("400x250")

# Etiquetas y entradas
label1 = tk.Label(ventana, text="Introduzca el multiplicando:")
label1.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana, text="Introduzca el multiplicador:")
label2.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack()

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=20)

# Función original
def multiplicar():
    multiplicando = float(entrada1.get())
    multiplicador = float(entrada2.get())
    resultado.config(
        text="Resultado de la multiplicacion: " + str(multiplicando * multiplicador)
    )

# Ejecutar al presionar Enter
ventana.bind(
    "<Return>",
    lambda event: multiplicar()
)

# Iniciar ventana
ventana.mainloop()
