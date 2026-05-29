import tkinter as tk

# Función LISTAS
def programa_lista():
    frutas = ["manzana", "pera", "uva"]

    texto = ""

    for fruta in frutas:
        texto += fruta + "\n"

    resultado.config(text=texto)

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa LISTAS")
ventana.geometry("300x250")

# Botón
boton = tk.Button(ventana, text="Mostrar frutas", command=programa_lista)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
