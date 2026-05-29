import tkinter as tk

# Función DO WHILE (simulado)
def programa_do_while():
    texto = ""
    contador = 1

    while True:
        texto += "HOLA MUNDO\n"
        contador += 1

        if contador > 1:
            break

    resultado.config(text=texto)

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa DO WHILE")
ventana.geometry("300x300")

# Botón
boton = tk.Button(ventana, text="Ejecutar", command=programa_do_while)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
