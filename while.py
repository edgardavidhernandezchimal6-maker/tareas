import tkinter as tk

# Función WHILE
def programa_while():
    contador = 1
    texto = ""

    while contador <= 5:
        texto += str(contador) + "\n"
        contador += 1

    resultado.config(text=texto)

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa WHILE")
ventana.geometry("300x300")

# Botón
boton = tk.Button(ventana, text="Mostrar números", command=programa_while)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
