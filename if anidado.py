import tkinter as tk

# Función IF ANIDADO
def programa_anidado():
    cal = int(entry_num.get())

    if cal >= 7:
        if cal >= 9:
            resultado.config(text="Excelente")
        else:
            resultado.config(text="Aprobado")
    else:
        resultado.config(text="Reprobado")

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa IF Anidado")
ventana.geometry("300x200")

# Etiqueta
label = tk.Label(ventana, text="Ingresa una calificación:")
label.pack(pady=10)

# Entrada
entry_num = tk.Entry(ventana)
entry_num.pack(pady=5)

# Botón
boton = tk.Button(ventana, text="Verificar", command=programa_anidado)
boton.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
