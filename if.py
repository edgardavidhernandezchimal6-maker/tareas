import tkinter as tk

# Función IF
def programa_if():
    num = int(entry_num.get())

    if num > 0:
        resultado.config(text="El número es positivo")

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa IF")
ventana.geometry("300x200")

# Etiqueta
label = tk.Label(ventana, text="Ingresa un número:")
label.pack(pady=10)

# Entrada
entry_num = tk.Entry(ventana)
entry_num.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Verificar", command=programa_if)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
