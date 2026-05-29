import tkinter as tk

# Función IF ELSE
def programa_if_else():
    num = int(entry_num.get())

    if num % 2 == 0:
        resultado.config(text="El número es par")
    else:
        resultado.config(text="El número es impar")

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa IF ELSE")
ventana.geometry("300x200")

# Etiqueta
label = tk.Label(ventana, text="Ingresa un número:")
label.pack(pady=10)

# Entrada
entry_num = tk.Entry(ventana)
entry_num.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Verificar", command=programa_if_else)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
