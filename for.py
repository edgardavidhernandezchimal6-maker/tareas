import tkinter as tk

# Función FOR
def programa_for():
    texto = ""

    for i in range(1, 11):
        texto += str(i) + "\n"

    resultado.config(text=texto)

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa FOR")
ventana.geometry("300x300")

# Botón
boton = tk.Button(ventana, text="Mostrar números", command=programa_for)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
